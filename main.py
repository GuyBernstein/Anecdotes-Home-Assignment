import asyncio

from fastapi import FastAPI
import httpx

app = FastAPI()

USERS_API = "https://dummyjson.com/users"
LOGIN_API = "https://dummyjson.com/auth/login"
POSTS_API = "https://dummyjson.com/posts"
COMMENTS_API = "https://dummyjson.com/comments/post"

@app.get("/get-first-valid-user")
async def get_first_valid_user():

    async with httpx.AsyncClient() as client:
        users_response = await client.get(USERS_API)
        users_response.raise_for_status()
        users = users_response.json()["users"]

        for user in users:
            login_payload = {
                "username": user["username"],
                "password": user["password"],
                "expiresInMins": 30
            }

            login_response = await client.post(
                LOGIN_API,
                json=login_payload,
                headers={"Content-Type": "application/json"}
            )

            if login_response.status_code == 200:
                login_data = login_response.json()
                result = {
                    "firstName": user["firstName"],
                    "lastName": user["lastName"],
                    "username": user["username"],
                    "password": user["password"],
                    "auth": login_data
                }

                return result

    return {"error": "No valid login found"}

@app.get("/get-60-posts")
async def get_60_posts():
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{POSTS_API}?limit=60&skip=0&select=title,reactions,userId"
        )
        response.raise_for_status()
        data = response.json()
        posts = [{"id": post["id"], "title": post["title"]} for post in data["posts"]]

    return {"posts": posts}

@app.get("/get-60-posts-with-comments")
async def get_60_posts_with_comments():
    async with httpx.AsyncClient() as client:
        # Step 1: Get 60 posts
        posts_response = await client.get(f"{POSTS_API}?limit=60&skip=0")
        posts_response.raise_for_status()
        posts_data = posts_response.json()["posts"]

        # Step 2: Define coroutine to fetch comments for one post
        async def fetch_comments(post):
            res = await client.get(f"{COMMENTS_API}/{post['id']}")
            res.raise_for_status()
            comments = res.json().get("comments", [])
            return {
                "id": post["id"],
                "title": post["title"],
                "comments": comments
            }

        # Step 3: Fetch all comments concurrently
        results = await asyncio.gather(*(fetch_comments(post) for post in posts_data))
        return {"posts": results}
