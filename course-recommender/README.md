# Course network graphs and recommender

Single-page app (`index.html`, open in a browser) built from a course survey: 36 students each listed three favorite courses.

- **Students tab**: students linked by shared favorite courses.
- **Courses tab**: courses linked when the same student picked both.
- **Recommender tab**: type a name, get up to five courses chosen by similar classmates.

`rows.txt` holds the cleaned responses, `build.py` normalizes course codes (DPI-851M, DPI 851 M and DPI-851 become DPI-851) and writes `data.json`, which is embedded in `index.html`.
