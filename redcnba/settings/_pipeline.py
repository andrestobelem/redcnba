PIPELINE_ENABLED = False

PIPELINE_CSS = {
    'bootstrap': {
        'source_filenames': (
            'exalumnos/less/bootstrap.less',
        ),
        'output_filename': 'exalumnos/css/bootstrap.min.css',
    },

    'selectize': {
        'source_filenames': (
            'exalumnos/selectize/less/selectize.less',
            'exalumnos/selectize/less/selectize.default.less',
            #'exalumnos/selectize/less/plugins/remove_button.less',
            #'exalumnos/selectize/less/selectize.bootstrap3.less',
        ),
        'output_filename': 'exalumnos/css/selectize.min.css',
    },

}

PIPELINE_JS = {

    'jquery': {
        'source_filenames': (
            'exalumnos/js/lib/jquery-2.1.0.js',
        ),
        'output_filename': 'exalumnos/js/jquery.min.js',
    },

    'bootstrap': {
        'source_filenames': (
            'exalumnos/bootstrap/js/alert.js',
            'exalumnos/bootstrap/js/collapse.js',
            'exalumnos/bootstrap/js/dropdown.js',
            'exalumnos/bootstrap/js/modal.js',
            'exalumnos/bootstrap/js/tabs.js',
            'exalumnos/bootstrap/js/tooltip.js',
            'exalumnos/bootstrap/js/popover.js',
            'exalumnos/bootstrap/js/typeahead.js',
        ),
        'output_filename': 'exalumnos/js/bootstrap.min.js',
    },

    'bootstrap-wizard': {
        'source_filenames': (
            'exalumnos/js/lib/jquery.bootstrap.wizard.js',
        ),
        'output_filename': 'exalumnos/js/lib/jquery.bootstrap.wizard.min.js',
    },


    'selectize': {
        'source_filenames': (
            'exalumnos/selectize/js/standalone/selectize.js',
        ),
        'output_filename': 'exalumnos/js/selectize.min.js',
    },
}

PIPELINE_COMPILERS = (
    'pipeline.compilers.less.LessCompiler',
)

PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.cssmin.CSSMinCompressor'

PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.uglifyjs.UglifyJSCompressor'
PIPELINE_UGLIFYJS_ARGUMENTS = "-m -c"
