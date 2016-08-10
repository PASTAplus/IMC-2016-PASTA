#!/bin/bash

scopeArg=$1
scope="knb-lter-$scopeArg"
baseUrl="http://pasta.lternet.edu/package"
baseDoiUrl="$baseUrl/doi/eml/$scope"
identifiersUrl="$baseUrl/eml/$scope"
identifiers="$(curl -s -X GET $identifiersUrl)"

for identifier in $identifiers; do
    newestRevisionUrl="$identifiersUrl/$identifier?filter=newest"
    newestRevision="$(curl -s -X GET $newestRevisionUrl)"
    packageId="$scope.$identifier.$newestRevision"
    doiUrl="$baseDoiUrl/$identifier/$newestRevision"
    doi="$(curl -s -X GET $doiUrl)"
    echo $packageId,$doi
done
