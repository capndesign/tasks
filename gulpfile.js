var gulp = require('gulp'),
    autoprefixer = require('gulp-autoprefixer'),
    cssnano = require('gulp-cssnano'),
    rename = require('gulp-rename'),
    del = require('del'),
    sass = require('gulp-sass');

gulp.task('vendor', function() {
  return gulp.src('./app/static/src/css/vendor/*')
    .pipe(gulp.dest('./app/static/dist/css/vendor/'));
});

gulp.task('styles', function() {
  return gulp.src('./app/static/src/css/index.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(autoprefixer('last 2 version'))
    .pipe(gulp.dest('./app/static/dist/css'))
    .pipe(rename({suffix: '.min'}))
    .pipe(cssnano())
    .pipe(gulp.dest('./app/static/dist/css'))
});

gulp.task('sass:watch', function () {
  gulp.watch('./app/static/src/css/**/*.scss', ['styles']);
});

gulp.task('clean', function() {
    return del(['./app/static/dist/css', './app/static/dist/js', './app/static/dist/img']);
});

gulp.task('default', ['clean'], function() {
  gulp.start('vendor', 'styles');
});