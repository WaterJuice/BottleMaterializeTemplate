#!/usr/bin/env python3

from __future__ import print_function
from bottle import route, run, default_app, static_file, TEMPLATES, error, template
import uuid
import os

@route('/')
def MainPage():
    # Create a new guid for fun!
    guid = str(uuid.uuid1())
    TEMPLATES.clear()
    # Use mainpage.html as a template with the value GUID set to the guid.
    return template( ScriptDir+'/templates/mainpage.html', GUID=guid)

# Handle the resources directory. This is just static files served
@route('/resources/<filename>')
def ResourceDir(filename):
    return static_file( filename, root=ScriptDir+'/resources' )

# Handle the error pages
def ErrorPage( ErrorNum, ErrorMessage ):
    TEMPLATES.clear()
    return template( ScriptDir+'/templates/error.html', ERROR=ErrorNum, MESSAGE=ErrorMessage )

@error(400)
def Error400(error): return ErrorPage( 400, 'Bad Request' )
@error(401)
def Error401(error): return ErrorPage( 401, 'Unauthorised' )
@error(403)
def Error403(error): return ErrorPage( 403, 'Forbidden' )
@error(404)
def Error404(error): return ErrorPage( 404, 'Not Found' )
@error(405)
def Error405(error): return ErrorPage( 405, 'Method Not Allowed' )
@error(500)
def Error500(error): return ErrorPage( 500, 'Internal Server Error' )


# Get the directory of the script so we can find resources relative to it
ScriptDir = os.path.dirname(os.path.realpath(__file__))

application = default_app()

# If run from command line directly start a bottle instance on port 8080
if __name__ == "__main__":
    run(host='0.0.0.0', port=8080)
