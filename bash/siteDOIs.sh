#!/bin/bash

scopeArg=$1
scope="knb-lter-$scopeArg"
baseUrl="https://pasta.lternet.edu"
identifiersUrl="$baseUrl/package/eml/$scope"
identifiers="$(curl -s -X GET $identifiersUrl)"

for identifier in $identifiers; do
    revisionsUrl="$identifiersUrl/$identifier"
    revisions="$(curl -s -X GET $revisionsUrl)"

    for revision in $revisions; do
        packageId="$scope.$identifier.$revision"
        doiUrl="$baseUrl/package/doi/eml/$scope/$identifier/$revision"
        doi="$(curl -s -X GET $doiUrl)"
        echo $packageId,$doi
    done

done
