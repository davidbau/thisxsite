# This X does not exist website

1. Put any number of png files in any number of subdirectories.
    They should all have filenames that end in `.png`.
2. Run `./setup.sh` to create a `choices.txt` file that lists them all.
3. Put this directory, including its `.htaccess` file, into any
    apache server which has had CGI enabled (e.g., `sudo a2enmod cgi`)
    and which enables `.htaccess` overrides (e.g., `AllowOverride all`).
4. Visiting the directory on the webserver should show you a random image.
