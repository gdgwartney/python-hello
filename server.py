"""
Pyramid web server application for personalized greetings.

This module implements a simple HTTP server using the Pyramid web framework.
It serves a personalized greeting message on the root route, with the name
configurable via environment variables.

Environment Variables:
    PORT: The port number for the server to listen on (default: 8001)
    NAME: The name to include in the greeting (default: "world")

Example:
    $ PORT=8080 NAME=Alice python server.py
    $ curl http://localhost:8080/
    Good morning, Alice!
"""

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os


def hello_world(request):
    """
    Handle HTTP requests and return a personalized greeting.

    This view function processes incoming HTTP requests on the root route
    and generates a greeting message. The name in the greeting is read from
    the NAME environment variable, defaulting to "world" if not set or empty.

    Args:
        request: The Pyramid request object containing HTTP request data.

    Returns:
        Response: A Pyramid Response object containing the greeting message
                  with a trailing newline.

    Example:
        With NAME="Alice": Returns "Good morning, Alice!\n"
        Without NAME: Returns "Good morning, world!\n"
    """
    # Retrieve the name from environment variable
    name = os.environ.get('NAME')

    # Use default name if environment variable is not set or empty
    if name == None or len(name) == 0:
        name = "world"

    # Construct the greeting message
    message = "Good morning, " + name + "!\n"

    return Response(message)


if __name__ == '__main__':
    # Read server port from environment variable, defaulting to 8001
    port = int(os.environ.get("PORT"))

    # Configure the Pyramid application
    with Configurator() as config:
        # Define the root route named 'hello'
        config.add_route('hello', '/')

        # Associate the hello_world view function with the 'hello' route
        config.add_view(hello_world, route_name='hello')

        # Create the WSGI application
        app = config.make_wsgi_app()

    # Create a simple WSGI server bound to all network interfaces (0.0.0.0)
    server = make_server('0.0.0.0', port, app)

    # Start the server and run indefinitely until interrupted
    server.serve_forever()
