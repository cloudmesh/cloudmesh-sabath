from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE
from cloudmesh.shell.command import map_parameters
from cloudmesh.common.parameter import Parameter
from cloudmesh.common.variables import Variables
from cloudmesh.common.util import banner
from cloudmesh.common.FlatDict import FlatDict



class SabathCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_sabath(self, args, arguments):
        """
        ::

          Usage:
                sabath list
                sabath fetch [--name=NAME] [--data=DATA]
                sabath info [--name=NAME]
                sabath run [--name=NAME]
                sabath md [--name=NAME]


          The cloudmesh implementation of sabath introduces the concept of a name for the surrogate

          This command does some useful things.

          Arguments:
              FILE   a file name
              PARAMETER  a parameterized parameter of the form "a[0-3],a5"

          Options:
              -f      specify the file

          Description:

            > cms sabath --parameter="a[1-2,5],a10"
            >    example on how to use Parameter.expand. See source code at
            >      https://github.com/cloudmesh/cloudmesh-sabath/blob/main/cloudmesh/sabath/command/sabath.py
            >    prints the expanded parameter as a list
            >    ['a1', 'a2', 'a3', 'a4', 'a5', 'a10']

            > sabath exp --experiment=a=b,c=d
            > example on how to use Parameter.arguments_to_dict. See source code at
            >      https://github.com/cloudmesh/cloudmesh-sabath/blob/main/cloudmesh/sabath/command/sabath.py
            > prints the parameter as dict
            >   {'a': 'b', 'c': 'd'}

        """


        # arguments.FILE = arguments['--file'] or None

        # switch debug on

        variables = Variables()
        variables["debug"] = True

        map_parameters(arguments,
                       "name",
                       "parameter",
                       "experiment")

        #VERBOSE(arguments)

        arguments.config = arguments.config or "config.yaml"
        arguments = Parameter.parse(arguments)
        #                             parameter='expand',
        #                             experiment='dict',
        #                             COMMAND='str')


        VERBOSE(arguments)


        #
        # It is important to keep the programming here to a minimum and any substantial programming ought
        # to be conducted in a separate class outside the command parameter manipulation. If between the
        # elif statement you have more than 10 lines, you may consider putting it in a class that you import
        # here and have propper methods in that class to handle the functionality. See the Manager class for
        # an example.
        #

        try:
            name = arguments.name

            if arguments.list:
                print("list")

            elif arguments.fetch:
                print("fetch", name)

            elif arguments.info:
                print("fetch", name)

            elif arguments.run:
                print("fetch", name)

            elif arguments.md:
                f = FlatDict(sep=".")
                content = f.load(content=arguments.config)
                pprint (f.__dict__)

                banner("Docuentation", color="RED")
                from cloudmesh.sabath.extension import to_md
                print(to_md(f.dict))

        except Exception as e:
            Console.error(e)
        #
        # Console.error("This is just a sample of an error")
        # Console.warning("This is just a sample of a warning")
        # Console.info("This is just a sample of an info")
        #
        # Console.info(" You can witch debugging on and off with 'cms debug on' or 'cms debug off'")

        return ""
