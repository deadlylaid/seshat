import pkgutil


def import_submodules(context, root_module, path):
    for loader, module_name, is_pkg in pkgutil.walk_packages(path, root_module + '.'):
        module = __import__(module_name, globals(), locals(), ['__name__'])
        for k, v in vars(module).items():
            if not k.startswith('_'):
                context[k] = v
        context[module_name] = module
