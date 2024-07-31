# ![YouTube Logo](https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png) YouTube Remote Uploader ![Python Logo](https://www.python.org/static/community_logos/python-logo.png)

![GitHub release (latest by date)](https://img.shields.io/github/v/release/SH20RAJ/youtube-remote-uploader)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/SH20RAJ/youtube-remote-uploader/upload_video.yml)
![GitHub](https://img.shields.io/github/license/SH20RAJ/youtube-remote-uploader)

YouTube Remote Uploader is a tool that automates the process of downloading videos from remote URLs and uploading them to YouTube using the YouTube Data API. This tool is particularly useful for batch processing and scheduled uploads using GitHub Actions.

## Features

- 🚀 Download videos from remote URLs
- 📹 Upload videos to YouTube with metadata (title, description, tags, etc.)
- 📦 Batch processing of multiple videos
- 🔄 Automation with GitHub Actions

## Getting Started

### Prerequisites

- 🐍 Python 3.x
- 📦 Google API Client Library
- 🔐 GitHub repository with necessary permissions and secrets

### Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/SH20RAJ/youtube-remote-uploader.git
   cd youtube-remote-uploader
   ```

2. **Install required libraries:**

   ```sh
   pip install -r requirements.txt
   ```

3. **Set up Google API credentials:**

   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project or select an existing project.
   - Enable the YouTube Data API v3 for your project.
   - Create OAuth 2.0 credentials and download the `credentials.json` file.
   - Save `credentials.json` in the root directory of the project.

4. **Set up GitHub secrets:**

   - Go to your GitHub repository settings.
   - Navigate to **Settings > Secrets and variables > Actions**.
   - Add a new secret named `GOOGLE_CREDENTIALS` with the contents of your `credentials.json` file.

### Usage

1. **Update `videos.json` with your video URLs and metadata:**

   ```json
   [
       {
           "url": "https://example.com/video1.mp4",
           "title": "Video Title 1",
           "description": "Description for Video 1",
           "tags": ["tag1", "tag2"],
           "category_id": "22",
           "privacy_status": "public"
       },
       {
           "url": "https://example.com/video2.mp4",
           "title": "Video Title 2",
           "description": "Description for Video 2",
           "tags": ["tag3", "tag4"],
           "category_id": "22",
           "privacy_status": "public"
       }
   ]
   ```

2. **Run the script locally:**

   ```sh
   python upload_video.py
   ```

3. **Automate with GitHub Actions:**

   Create a `.github/workflows/upload_video.yml` file with the following content:

   ```yaml
   name: Upload Videos to YouTube

   on:
     push:
       branches:
         - main
     workflow_dispatch:

   jobs:
     upload_videos:
       runs-on: ubuntu-latest

       steps:
       - name: Checkout repository
         uses: actions/checkout@v3

       - name: Set up Python
         uses: actions/setup-python@v4
         with:
           python-version: '3.x'

       - name: Install dependencies
         run: |
           python -m pip install --upgrade p
           pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client requests

       - name: Set up Google Credentials
         run: echo "${{ secrets.GOOGLE_CREDENTIALS }}" > credentials.json

       - name: Run upload script
         run: python upload_video.py
   ```

   Push your changes to the repository:

   ```sh
   git add .
   git commit -m "Set up GitHub Actions workflow for video upload"
   git push origin main
   ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
