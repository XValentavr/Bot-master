"""
This module use amoCRM api to enter data
"""
import execjs
import js2py

un = """
function sample()
{
    console.log('hello')
}
"""
js2py.eval_js(un)()
