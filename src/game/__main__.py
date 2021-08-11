import logging 
import datetime
import click


from game.game import Game

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()
current_time_stamp = datetime.datetime.utcnow().strftime("%Y-%m-%d_%H_%M_%S")


def set_logging(debug=False):
    """ set up logging """
    if debug:
        log.setLevel(logging.DEBUG)
    else:
        log.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s   - %(message)s"
    )
    for handler in log.handlers:
        handler.setFormatter(formatter)


@click.command()
@click.option("--debug", "-v", is_flag=True, default=False, help="Set logging to debug")
@click.option("--width", "-w", default=900, help="Set default width of the app")
@click.option("--height", "-h", default=500, help="Set default height of the app")
@click.option("--caption", "-c", default="Provide a Caption", help="Set default height of the app")
def main(debug, width, height, caption):
    """
    Entry point to run the game.
    """
    set_logging(debug)
    game = Game(width, height, caption)
    game.run()


if __name__ == "__main__":
    main()
