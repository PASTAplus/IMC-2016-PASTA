#!/bin/bash

scopeArg=$1
scope="knb-lter-$scopeArg"
baseUrl="https://pasta.lternet.edu"
identifiersUrl="$baseUrl/package/eml/$scope"
identifiers="$(curl -s -X GET $identifiersUrl)"

for identifier in $identifiers; do
    newestRevisionUrl="$identifiersUrl/$identifier?filter=newest"
    newestRevision="$(curl -s -X GET $newestRevisionUrl)"
    packageId="$scope.$identifier.$newestRevision"
    doiUrl="$baseUrl/package/doi/eml/$scope/$identifier/$newestRevision"
    doi="$(curl -s -X GET $doiUrl)"
    echo $packageId,$doi
done
