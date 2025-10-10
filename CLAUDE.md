# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a simple Python web server using the Pyramid web framework. It serves a "Hello, [name]!" greeting on the root route.

## Development Commands

- **Install dependencies**: `pip install -r requirements.txt`
- **Run the server**: `PORT=8080 NAME=World python server.py`
  - The server requires the `PORT` environment variable to be set
  - The `NAME` environment variable is optional and defaults to "world"
- **Access the server**: `http://localhost:8080/` (or whatever port you specified)

## Architecture

### server.py

The main application file contains:
- `hello_world(request)`: View function that returns a greeting message. Reads the name from the `NAME` environment variable (server.py:6-11)
- Main block: Configures the Pyramid application, sets up routing, and starts the WSGI server on 0.0.0.0 (server.py:13-20)

### Configuration

The application is configured via environment variables:
- `PORT` (required): The port number the server listens on
- `NAME` (optional): The name to include in the greeting (defaults to "world")
