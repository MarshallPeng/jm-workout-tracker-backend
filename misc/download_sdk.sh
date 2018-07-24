#!/usr/bin/env bash

# Script to firebase sdk key so that tests can be run

if [[ $SDK_URL ]]
then
    echo "SDK detected - downloading..."
    # we're using curl instead of wget because it will not
    # expose the sensitive uri in the build logs:
    curl ${SDK_URL} -o src/config/jm-workout-tracker-firebase-adminsdk.json -L
else
    echo "SDK url not set. Please set environment variable and try again."
fi