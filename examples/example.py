
"""
                        Before you read any further, I recommend associating
                        the EVS file type with Python files in your IDE so
                        you can see all the useful syntax highlighting and
                        even use auto-completion and inspection. 
                        
                        You can also just use the '.py' extension if you 
                        prefer, which I've used here so that you can see the 
                        syntax highlighting on GitHub.

                        You can ask me anything on the ?ServerName? Dark
                        Souls modding Discord. I'm sure there are bugs and
                        typos; I haven't tried every single instruction and
                        test yet. You can raise these on GitHub as well.

                        All the best with your event modding, and I hope this
                        helps.
                                                                   Grimrukh
"""

# This star import is purely so your intelli-sense can pick up all the instructions, tests, and other EVS wrapper
# functions. It is ignored by the compiler and can actually be removed entirely if you don't care about auto-completion
# or intelli-sense inspection, etc.
from emevd import *

# This import actually matters. You should define your constants in a separate Python script, and import them here.
# See 'example_constants.py' for examples. You can then use these constants in your EVS script below. The intent is
# that you can carefully control which constants (particularly Flags) each map's script has access to, which will
# reduce the chances of accidental, crippling, silent bugs caused by using the wrong one. Note that unlike the general
# star import above, any imports here do matter to the compiler and will determine what constants it has access to.
from examples.example_constants import *

# (I'll consider adding support for you to directly define your constants here, but it complicates things, and you
# should really be keeping them separate anyway.)

# After constant imports, the rest of the EVS script is strictly comprised of function declarations - one per event.
# I'll go over the components of a couple of simple examples from Firelink Shrine in Daughters of Ash.


# EVENT NAME: The name of the function should be the event name. This is completely up to you and will be stripped from
# the binary EMEVD. After creating an EmevdCompiler() instance, you can look at all of your events with the `events`
# attribute, which has event names for keys. You can also call the event name as a shortcut for calling RunEvent on
# its name or ID, with arguments (if it has any).

# This event happens to be the constructor, which I've put in caps as a note to myself that I shouldn't be actually
# calling this anywhere. In future, I'll probably force you to call this CONSTRUCTOR and force its ID to be 0 so you
# know what you're doing. (There's also a PRECONSTRUCTOR with ID 50, which is called before the CONSTRUCTOR and
# handles things that are assumed to be done by the CONSTRUCTOR - notably, updating NPC story flags.)
def CONSTRUCTOR():
    """ 0: Constructor run on map load. """

    PullOutMeltedIronKey()
    # This event takes arguments when run, which creates an 'instance' of the event that has specific constants.
    # The names and types of the arguments are defined in the event argument list. You can only use positional
    # arguments here, as order matters, and the first argument must always be the slot number.
    DespawnChanneler(0, CHARACTERS.DepthsChanneler)


# Here's a better example of an event name.
def PullOutMeltedIronKey():
    # The event must start with a triple-quoted Python docstring. It should look like this:
    # """ [ThisEventFlagName] EventID[: description] """
    # The EventID is compulsory, but the flag name and description are optional. The description will be attached to
    # the event data in EmevdCompiler.events. You can actually use this flag name elsewhere in your script, as they're
    # all collected by the compiler before intepreting code, but if you want to access the flag from another script or
    # make your intelli-sense happy, you'll still need to put the same flag name and ID in your constants.
    """ MeltedIronKeyReceived 11000112: Inspect door to Depths from Blighttown and pull out Melted Iron Key. """

    # Simple conditional check that terminates the event right at the start if this event's flag (the one given in the
    # docstring above) is already on. THIS_FLAG is an EVS constant you can use to check the flag of this event. Look at
    # the other constants in emevd.constants. For example, you can 'return RESTART' to restart the event.

    # If you look at the actual verbose output of your script, you'll notice that these two lines are compressed into a
    # single instruction that ends the event if the flag is enabled. The EVS compiler works hard to use as few lines of
    # EMEVD as necessary, and particularly tries to avoid creating conditions whenever possible.
    if THIS_FLAG:
        return  # (You'll see this two-line combo a lot in 'one-off' events.)

    # Our first actual instruction (aside from running an event). This stops the player from being able to activate the
    # door via its ObjAct event (specified in the MSB file). An objact_param_id of -1 finds the param that shares the
    # door's ID.
    DisableObjectActivation(OBJECTS.DepthsDoor, -1)

    # The Await() instruction is one of the most important. It takes a test as an argument, and will halt the event
    # logic until the test is met. We're kicking things off with one of the most complex tests, which waits for the
    # player to press A when a dialog is presented. Note that the dialog is implicitly created by this test, according
    # to its arguments (e.g. it only displays when you are closer than 'max_distance'). It also won't be created until
    # all earlier conditions in the test are met, if there are any.
    Await(
        # You can pass in positional arguments and/or keyword arguments to any instruction or test. I've used a mixture
        # of both here, and intentionally put the keywords out of order, so you can see that it works. This particular
        # test has a lot of optional arguments. You can see their default values in `tests.pyi`.
        DialogPromptActivated(TEXT.Open, anchor_entity=OBJECTS.DepthsDoor, facing_angle=60.0,
                              model_point=100, max_distance=1.5)
    )

    # I've made the button-controlling arguments optional here, as I usually display dialogs with no buttons (they
    # don't do anything).
    DisplayDialog(TEXT.SomethingInDoor, anchor_entity=OBJECTS.DepthsDoor)

    # We halt here for one second. Note that I like to pass floats where they're expected, but integers work fine too.
    Wait(1.0)

    # Again, note that the prompt won't appear until the game actually cares about the player activating it.
    Await(
        DialogPromptActivated(TEXT.RemoveItemFromDoor, anchor_entity=OBJECTS.DepthsDoor, facing_angle=60.0,
                              model_point=100, max_distance=1.5)
    )

    # This instruction defaults to 'host_only', which you can set to False to share the love with your summons.
    AwardItemLot(ITEMLOT.InDepthsDoor)

    Wait(2.0)

    # The player can open the door again.
    EnableObjectActivation(OBJECTS.DepthsDoor, -1)

    # As always, when the processor reaches the end of the event function, the event flag that matches the event's ID
    # (in our docstring) is enabled. (Note that flags that end in 5*** are disabled on every map load.)


# You can add this decorator to make this event restart when you rest at a bonfire. There's also a 'NeverRestart'
# decorator, but that's applied by default if you leave it out. (The third decorator, 'UnknownRestart', is used only
# by skeleton assembly scripts and we haven't figured out exactly how it works yet. You're welcome to experiment.)
@RestartOnRest
def DespawnChanneler(channeler: int):
    # Use type annotations ('int' above) to specify the type of the argument, which is required to determine the
    # binary structure of the argument data. You can name the arguments anything you want, but I recommend lower case
    # to distinguish them from constants and functions. I've also added 'short', 'char', etc. as global constants so
    # you can specify those smaller-size arguments.
    """ 11000860: Channeler appears until you have been to the Painted World. """
    # Note that it's a bad idea to give a flag name to an event that takes arguments, as the actual flag value that is
    # automatically enabled when the event finishes will have the slot number added to it.

    if not FLAGS.PaintedWorldVisited:
        return

    # This is pointless, but just demonstrating the built-in map name constants you can use.
    Await(InsideMap(DEPTHS))

    # Note use of our argument here.
    DisableCharacter(channeler)
    Kill(channeler)
    # Small aside, but FROM likes to kill 'de-spawned' enemies after disabling them, for some reason. There's an
    # optional argument, 'award_souls', that is False by default, which you can use to have the game give you the reward
    # souls that rightfully belong to this script.

    # When this event finishes, flag 11000860 + slot will be enabled. You can query the current slot's flag with
    # THIS_SLOT_FLAG, rather than THIS_FLAG, which will ignore the slot and use the base event ID (11000860 here).


# To add to the above, this RestartOnRest decorator is most often used with events that control the appearance of
# enemies. (NPC appeareance is usually controlled in event 50, the PRECONSTRUCTOR, which seems to restart on rest
# by default.) Enemies will otherwise respawn as soon as you rest, despite being disabled once when the map loaded.
@RestartOnRest
def event11005100(trigger_region_1: Region, trigger_region_2: Region, slime: Character, delay: float):
    # Here we see that you can actually specify the exact DS type of your arguments. This is required to use them
    # implicitly in condition tests, because we need to know exactly what they are.
    """ 11005100: Slime ambushes. Now takes two region triggers rather than one. """

    # Here's an actual use of THIS_SLOT_FLAG. In this case, it prevents the slime from falling if it's already fallen.
    # Because this event uses a temporary 5000 flag, this logic will probably always happen unless you run very far
    # away from the slime to despawn it, then run back without reloading.
    if not THIS_SLOT_FLAG:
        DisableGravity(slime)
        DisableCollision(slime)
        if trigger_region_2 == 0:
            # Nested IF! Comparison test! Look at the verbose result. Anything with a value can be used in a numeric
            # comparison, but it's generally only used to query event arguments, because comparing two predefined
            # constants and expecting to ever be surprised is a lost cause. Also note the built-in PLAYER constant,
            # which is always equal to 10000. (10001-10006 refer to summoned players. Not sure about invaders...)
            Await(trigger_region_1 or IsAttacked(slime, PLAYER))
        else:
            # If were were writing in raw EMEVD, we would probably just conditionally skip over a single line that adds
            # trigger_region_2 to the condition if it is not equal to 0. (That's what I did in Daughters of Ash.) But
            # this happens so rarely (and doesn't even affect performance, just script length) that I don't think it's
            # a good enough reason to bother implementing front-end condition control. The whole point is that you
            # never have to manually build a condition or calculate a line skip again.
            Await(trigger_region_1 or trigger_region_2 or IsAttacked(slime, PLAYER))
        Wait(delay)

    EnableGravity(slime)
    EnableCollision(slime)
    ResetStandbyAnimationSettings(slime)


# There's plenty of other cool EVS features, like manually creating a Condition() and setting 'hold=True' to force the
# condition manager to keep it around when you're done so you can use it again as a 'finished' condition. There are
# also FlagRange objects, which you can pass to instructions like EnableFlagRange and EnableRandomFlagInRange. You can
# use all(conditions) and any(conditions) to try to construct elaborate chain skips that can often mimic complex
# conditions (these are used often in the CONSTRUCTOR and PRECONSTRUCTOR - in fact, FROM *never* uses conditions in
# either of these events). And a bunch of other stuff, like implicitly checking if a player owns a weapon (for example)
# by writing 'if WEAPONS.BlackKnightHalberd: ...'.
