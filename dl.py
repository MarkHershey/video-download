from pathlib import Path
import subprocess
import logging
import sys
import os


def main():
    # get logger
    logger = logging.getLogger(name="Main")
    logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)

    # check if there is a 'Downloads' directory under user's home folder.
    home = str(Path.home())
    exist = os.path.exists(os.path.join(home, "Downloads"))

    if exist:  # set it as download folder
        template = os.path.join(home, "Downloads") + "/%(title)s_%(resolution)s.%(ext)s"
        logger.info(f"Video will be downloaded into {os.path.join(home, 'Downloads')}")
    else:  # set download folder under current working directory
        cwd = os.path.dirname(os.path.abspath(__file__))
        template = cwd + "/Downloads/%(title)s_%(resolution)s.%(ext)s"
        logger.info(f"Video will be downloaded into {cwd + '/Downloads'}")

    try:
        video_link = sys.argv[1]
    except IndexError:
        logger.error("You must provide a video link as an argument.")
        logger.info("youtube-dl is not called due to this error.")
        return

    try:
        threads_num = sys.argv[2]
        if not threads_num.isdigit():
            raise TypeError(
                f"'{threads_num}' is not an integer. Number of Threads for aria2 must be a positive integer."
            )
        if int(threads_num) <= 0:
            raise ValueError("Invalid Number of Threads for aria2")
    except IndexError:
        threads_num = False
        logger.info("aria2 threads number is not provided.")
        logger.info(
            "aria2 will not be used for this download due to no second argument is supplied."
        )
    except Exception as err:
        logger.error(err)
        logger.info("youtube-dl is not called due to this error.")
        return

    if threads_num:
        logger.info(f"Calling youtube-dl")
        logger.info(f"Using aria2 with {threads_num} threads")

        subprocess.call(
            [
                "youtube-dl",
                "-f",
                "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
                "-o",
                template,
                "--external-downloader",
                "aria2c",
                "--external-downloader-args",
                "-x" + threads_num,
                video_link,
            ]
        )
    else:
        logger.info(f"Calling youtube-dl without aria2")

        subprocess.call(
            [
                "youtube-dl",
                "-f",
                "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
                "-o",
                template,
                video_link,
            ]
        )


if __name__ == "__main__":
    main()
