#!/bin/bash

IFS=$' \r\n' read method path protocol

# Discard headers
while read header && [[ "$header" != $'\r' && "$header" != "" ]]; do :; done

file="./www/${path#/}"

if [[ "$method" == "GET" ]]; then
  if [[ -f "$file" ]]; then
    length=$(wc -c <"$file")
    echo -ne "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: $length\r\n\r\n"
    cat "$file"
  else
    echo -ne "HTTP/1.1 404 Not Found\r\nContent-Length: 0\r\n\r\n"
  fi
else
  echo -ne "HTTP/1.1 400 Bad Request\r\nContent-Length: 0\r\n\r\n"
fi

