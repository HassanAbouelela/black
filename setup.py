# assert sys.version_info >= (3, 6, 2), "black requires Python 3.6.2+"
#
#
# def get_long_description() -> str:
#     return (
#         (CURRENT_DIR / "README.md").read_text(encoding="utf8")
#         + "\n\n"
#         + (CURRENT_DIR / "CHANGES.md").read_text(encoding="utf8")
#     )
#
#
# USE_MYPYC = False
# # To compile with mypyc, a mypyc checkout must be present on the PYTHONPATH
# if len(sys.argv) > 1 and sys.argv[1] == "--use-mypyc":
#     sys.argv.pop(1)
#     USE_MYPYC = True
# if os.getenv("BLACK_USE_MYPYC", None) == "1":
#     USE_MYPYC = True
#
# if USE_MYPYC:
#     mypyc_targets = [
#         "src/black/__init__.py",
#         "src/blib2to3/pytree.py",
#         "src/blib2to3/pygram.py",
#         "src/blib2to3/pgen2/parse.py",
#         "src/blib2to3/pgen2/grammar.py",
#         "src/blib2to3/pgen2/token.py",
#         "src/blib2to3/pgen2/driver.py",
#         "src/blib2to3/pgen2/pgen.py",
#     ]
#
#     from mypyc.build import mypycify
#
#     opt_level = os.getenv("MYPYC_OPT_LEVEL", "3")
#     ext_modules = mypycify(mypyc_targets, opt_level=opt_level)
# else:
#     ext_modules = []
#
# setup(
#     use_scm_version={
#         "write_to": "src/_black_version.py",
#         "write_to_template": 'version = "{version}"\n',
#     },
#     long_description=get_long_description(),
#     long_description_content_type="text/markdown",
#     py_modules=["_black_version"],
#     ext_modules=ext_modules,
#     package_dir={"": "src"},
#     package_data={
#         "blib2to3": ["*.txt"],
#         "black": ["py.typed"],
#         "black_primer": ["primer.json"],
#     },
#     zip_safe=False,
#     test_suite="tests.test_black",
# )
