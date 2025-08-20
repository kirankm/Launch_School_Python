#!/opt/homebrew/bin/bash

read request_line
method=$(echo "$request_line" | awk '{print $1}')
path=$(echo "$request_line" | awk '{print $2}')
protocol=$(echo "$request_line" | awk '{print $3}')

# Discard remaining headers
while read -r header && [[ "$header" != $'\r' && "$header" != "" ]]; do :; done

file="./www/${path#/}"

if [[ "$method" == "GET" ]]; then
  if [[ -f "$file" ]]; then
    length=$(wc -c <"$file" | tr -d ' ')
    echo -ne "HTTP/1.1 200 OK\r\n"
    echo -ne "Content-Type: text/html\r\n"
    echo -ne "Content-Length: $length\r\n"
    echo -ne "\r\n"
    cat "$file"
  else
    echo -ne "HTTP/1.1 404 Not Found\r\nContent-Length: 0\r\n\r\n"
  fi
else
  echo -ne "HTTP/1.1 400 Bad Request\r\nContent-Length: 0\r\n\r\n"
fi

