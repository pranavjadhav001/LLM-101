import logging
from yachalk import chalk
import os

class GraphLogger:

    def __init__(self, name="Graph Logger", color="white"):
        "Set the log level (optional, can be DEBUG, INFO, WARNING, ERROR, CRITICAL)"

        log_level = os.environ.get("LOG_LEVEL", "INFO").upper()
        logging.basicConfig(level=log_level)

        ## Formatter
        self.time_format = "%Y-%m-%d %H:%M:%S"
        format = self.format(color)
        self.formatter = logging.Formatter(
            fmt=format,
            datefmt=self.time_format,
        )

        ## Handler
        handler = logging.StreamHandler()
        handler.setFormatter(self.formatter)

        ## Logger
        self.logger = logging.getLogger(name)
        self.logger.addHandler(handler)
        self.logger.propagate = False

    def getLogger(self):
        return self.logger

    def format(self, color: str):
        color_formats = {
            "black": chalk.black,
            "red": chalk.red,
            "green": chalk.green,
            "yellow": chalk.yellow,
            "blue": chalk.blue,
            "magenta": chalk.magenta,
            "cyan": chalk.cyan,
            "white": chalk.white,
            "black_bright": chalk.black_bright,
            "red_bright": chalk.red_bright,
            "green_bright": chalk.green_bright,
            "yellow_bright": chalk.yellow_bright,
            "blue_bright": chalk.blue_bright,
            "magenta_bright": chalk.magenta_bright,
            "cyan_bright": chalk.cyan_bright,
            "white_bright": chalk.white_bright,
            "grey": chalk.grey,
        }

        format_func = color_formats.get(color, chalk.white)
        return format_func("\n▶︎ %(name)s - %(asctime)s - %(levelname)s \n%(message)s\n")

# Example usage:
if __name__ == "__main__":
    logger = GraphLogger(name="ExampleLogger", color="blue").getLogger()
    logger.info("This is an info message.")
    logger.error("This is an error message.")

