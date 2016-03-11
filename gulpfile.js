var gulp = require('gulp'),
    autoprefixer = require('gulp-autoprefixer'),
    cssnano = require('gulp-cssnano'),
    rename = require('gulp-rename'),
    del = require('del'),
    uglify = require('gulp-uglify'),
    sass = require('gulp-sass'),
    babel = require('gulp-babel'),
    mainBowerFiles = require('main-bower-files'),
    gulpif = require('gulp-if'),
    concat = require('gulp-concat')
    ;

var srcDir = "./app/static/src/";
var distDir = "./app/static/dist/";

gulp.task('vendor', function() {
  return gulp.src(srcDir + 'css/vendor/*')
    .pipe(gulp.dest(distDir + 'css/vendor/'));
});

gulp.task('styles', function() {
  return gulp.src(srcDir + 'css/index.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(autoprefixer('last 2 version'))
    .pipe(gulp.dest(distDir + 'css'))
    .pipe(rename({suffix: '.min'}))
    .pipe(cssnano())
    .pipe(gulp.dest(distDir + 'css'))
});

gulp.task('bowerFiles', function() {
  return gulp.src(mainBowerFiles(), { base: './bower_components/' })
    .pipe(concat('vendor.js'))
    .pipe(gulp.dest(srcDir + 'js/'))
});

gulp.task('scripts', ['bowerFiles'], function() {
  return gulp.src(srcDir + 'js/*.js')
    .pipe(gulpif(/[.]babel.js$/, babel({
      presets: ['es2015']
    })))
    .pipe(gulpif(/[.]babel.js$/, rename(function(path){
      path.basename = path.basename.replace(".babel", "");
      return path;
    })))
    .pipe(gulp.dest(distDir + 'js/'))
    .pipe(rename({suffix: '.min'}))
    .pipe(uglify())
    .pipe(gulp.dest(distDir + 'js/'))
});

gulp.task('watch', function () {
  gulp.watch(srcDir + 'css/**/*.scss', ['styles']);
  gulp.watch(srcDir + 'js/**/*.js', ['scripts']);
});

gulp.task('clean', function() {
    return del([distDir + 'css', distDir + 'js', distDir + 'img']);
});

gulp.task('default', ['clean'], function() {
  gulp.start('vendor', 'styles', 'scripts');
});