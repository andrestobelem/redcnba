PIPELINE_ENABLED = False

PIPELINE_CSS = {
    'bootstrap': {
        'source_filenames': (
            'bower_components/less/bootstrap.less',
        ),
        'output_filename': 'css/bootstrap.min.css',
    },

    'selectize': {
        'source_filenames': (
            'bower_components/selectize/less/selectize.less',
            'bower_components/selectize/less/selectize.default.less',
            # 'exalumnos/selectize/less/selectize.bootstrap3.less',
        ),
        'output_filename': 'css/selectize.min.css',
    },

}

PIPELINE_JS = {
    'jquery': {
        'source_filenames': (
            'bower_components/jquery/dist/jquery.js',
        ),
        'output_filename': 'js/jquery.min.js',
    },

    'bootstrap': {
        'source_filenames': (
            'bower_components/bootstrap/js/alert.js',
            'bower_components/bootstrap/js/collapse.js',
            'bower_components/bootstrap/js/dropdown.js',
            'bower_components/bootstrap/js/modal.js',
            'bower_components/bootstrap/js/tabs.js',
            'bower_components/bootstrap/js/tooltip.js',
            'bower_components/bootstrap/js/popover.js',
        ),
        'output_filename': 'js/bootstrap.min.js',
    },

    # 'bootstrap-wizard': {
    # 'source_filenames': (
    # 'exalumnos/js/lib/jquery.bootstrap.wizard.js',
    #     ),
    #     'output_filename': 'exalumnos/js/lib/jquery.bootstrap.wizard.min.js',
    # },

    'selectize': {
        'source_filenames': (
            'bower_components/selectize/js/standalone/selectize.js',
        ),
        'output_filename': 'js/selectize.min.js',
    },

    # 'typeahead': {
    #     'source_filenames': (
    #         'bower_components/typeahead.js/dist/typeahead.bundle.js',
    #     ),
    #     'output_filename': 'js/typeahead.bundle.min.js',
    # },
}

PIPELINE_COMPILERS = (
    'pipeline.compilers.less.LessCompiler',
)

PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.cssmin.CSSMinCompressor'

PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.uglifyjs.UglifyJSCompressor'
PIPELINE_UGLIFYJS_ARGUMENTS = "-m -c"