import os
import logging
import fire
from discord_bot import DiscordBot
from firebase_admin import initialize_app, credentials, firestore


def serve(discord_bot_token: str, svc_path: str, parlai_websocket_url: str):
    """
    TODO
    """
    logger = logging.getLogger("socialis")
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = svc_path
    initialize_app(
        credentials.Certificate(
            svc_path,
        )
    )
    firestore_client = firestore.Client()
    logger.info(f"initialized Firebase with project {firestore_client.project}")
    DiscordBot(logger, firestore_client, parlai_websocket_url).run(discord_bot_token)


def main():
    """
    Starts socialis.
    """
    logging.basicConfig(level=logging.INFO)

    fire.Fire(serve)


if __name__ == "__main__":
    main()
