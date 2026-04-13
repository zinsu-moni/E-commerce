from dotenv import load_dotenv
import os
import cloudinary
import cloudinary.uploader

load_dotenv()

cloudinary_config = {
    "cloud_name": os.getenv("CLOUDINARY_CLOUD_NAME"),
    "api_key": os.getenv("CLOUDINARY_API_KEY"),
    "api_secret": os.getenv("CLOUDINARY_API_SECRET")
}

cloudinary.config(**cloudinary_config)

def upload_image(file, folder: str = "product") -> dict:
    result = cloudinary.uploader.upload(
        file,
        folder = folder,
        image_type = "image",
        transformation=[
            {"width": 800, "height": 800, "crop": "limit"},
            {"quality": "auto"},
            {"fetch_format": "auto"}
        ]
    )

    return {
        "url": result.get("secure_url"),
        "public_id": result.get("public_id")
    }

def delete_image(public_id: str) -> bool:
    result = cloudinary.uploader.destroy(public_id)
    return result.get("result") == "ok"

