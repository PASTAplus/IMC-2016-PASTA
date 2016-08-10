#!/bin/bash

scopeArg=$1
scope="knb-lter-$scopeArg"
baseUrl="http://pasta.lternet.edu/package"
baseDoiUrl="$baseUrl/doi/eml/$scope"
identifiersUrl="$baseUrl/eml/$scope"
identifiers="$(curl -s -X GET $identifiersUrl)"

for identifier in $identifiers; do
    revisionsUrl="$identifiersUrl/$identifier"
    revisions="$(curl -s -X GET $revisionsUrl)"

    for revision in $revisions; do
        packageId="$scope.$identifier.$revision"
        doiUrl="$baseDoiUrl/$identifier/$revision"
        doi="$(curl -s -X GET $doiUrl)"
        echo $packageId,$doi
    done

done
