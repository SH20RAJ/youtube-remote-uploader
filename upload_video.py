import os
import requests
import google.auth
import google.auth.transport.requests
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import json

# Set up OAuth 2.0 authorization
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def get_authenticated_service():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(google.auth.transport.requests.Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return build("youtube", "v3", credentials=creds)

def download_video(video_url, output_path):
    response = requests.get(video_url, stream=True)
    with open(output_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

def upload_video(service, video_file, title, description, tags, category_id, privacy_status):
    body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": category_id
        },
        "status": {
            "privacyStatus": privacy_status
        }
    }
    media = MediaFileUpload(video_file, chunksize=-1, resumable=True)
    request = service.videos().insert(
        part="snippet,status",
        body=body,
        media_body=media
    )
    response = request.execute()
    print(f"Video uploaded: {response['id']}")

def process_videos(video_urls):
    service = get_authenticated_service()
    for video in video_urls:
        video_url = video["url"]
        local_video_file = "temp_video.mp4"
        title = video["title"]
        description = video["description"]
        tags = video.get("tags", [])
        category_id = video.get("category_id", "22")
        privacy_status = video.get("privacy_status", "public")

        download_video(video_url, local_video_file)
        upload_video(service, local_video_file, title, description, tags, category_id, privacy_status)
        os.remove(local_video_file)

if __name__ == "__main__":
    with open("videos.json") as f:
        video_urls = json.load(f)
    process_videos(video_urls)
