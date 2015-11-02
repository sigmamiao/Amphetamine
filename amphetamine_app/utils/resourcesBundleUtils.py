#!/Users/Omega/pythonVenv/venv/bin python
# -*- coding:utf-8 -*-


"""
    Amphetamine.app

    Create on 15/10/17 17:00 By OmegaMiao

    resourcesBundleUtils.py
"""

from flask.ext.assets import Bundle, Environment
from .. import amphetamine_app

bundles = {
    'bootstrap_js': Bundle(
        'js/jquery.js',
        'js/jquery.json.min.js',
        # 'js/bootstrap.min.js',
        'js/bootstrapValidator.min.js',
        'js/flat-ui.min.js',
        'js/plugins/bootstrap-treeview.min.js'
        # 'js/radiocheck.js'

    ),
    'feature_js': Bundle(
        'js/testcase/testCaseValidation.js',
        'js/teststep/testStepValidation.js',
        'js/testcase/updateTestCase.js',
        'js/testcase/runTestCaseValidation.js',
        'js/teststep/updateTestStep.js',
        'js/exportTestSuite.js',
        'js/runTestSuite.js',
        'js/commonWidgetPretty.js',
        'js/testcase/runTestCase.js',
        'js/app/app.js'
    ),
    'bootstrap_css': Bundle(
        'css/bootstrap.min.css',
        # 'css/bootstrap-theme.css',
        'css/flat-ui.min.css',
        'css/bootstrapValidator.min.css',
        'css/main.css'
    )
}

assets = Environment(amphetamine_app)
assets.register(bundles)
