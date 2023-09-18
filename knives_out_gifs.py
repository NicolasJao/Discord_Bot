
import random as rand
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="/")


def randomgif():
    yeet = rand.randint(0, 52)

    giflist = [
        "https://tenor.com/view/coming-omw-almost-there-walk-chris-evans-gif-15433731",
        "https://tenor.com/view/do-this-more-chris-evans-more-often-knives-out-gif-15093976",
        "https://tenor.com/view/heinous-crime-horrible-tragic-daniel-craig-gif-15433728",
        "https://tenor.com/view/foul-play-suspect-foul-play-daniel-craig-knives-out-gif-15093979",
        "https://tenor.com/view/wink-igot-it-gotcha-gotchu-confident-gif-15437124",
        "https://tenor.com/view/chris-evans-eat-shit-definitely-gif-14486029",
        "https://tenor.com/view/chris-evans-wow-surprised-shocked-not-surpised-gif-14464535",
        "https://tenor.com/view/knives-out-movie-title-titles-movie-titles-gif-15093980",
        "https://tenor.com/view/ifound-it-delightful-iliked-it-enjoyable-it-was-great-linda-robinson-gif-15562576",
        "https://tenor.com/view/donut-doughnut-hole-knives-out-daniel-craig-benoit-blanc-gif-16770769",
        "https://tenor.com/view/chris-evans-huh-what-cute-handsome-gif-17113375",
        "https://tenor.com/view/daniel-craig-knives-out-detective-turn-around-gif-15065097",
        "https://tenor.com/view/looking-around-what-look-up-whats-that-knives-out-gif-14471937",
        "https://tenor.com/view/omg-scared-shocked-crying-are-you-serious-gif-14472021",
        "https://tenor.com/view/staring-disbelief-umm-wait-what-excuse-me-gif-14472030",
        "https://tenor.com/view/well-then-fireside-serious-benoit-blanc-daniel-craig-gif-14472027",
        "https://tenor.com/view/hmm-thinking-wondering-waiting-scheming-gif-15093836",
        "https://tenor.com/view/iknow-iknow-what-you-did-knives-out-gif-15093958",
        "https://tenor.com/view/eliminated-no-suspects-suspect-daniel-craig-knives-out-gif-15093959",
        "https://tenor.com/view/spill-spill-it-jamie-lee-curtis-knives-out-gif-15093965",
        "https://tenor.com/view/famous-youre-famous-so-famous-knives-out-gif-15093968",
        "https://tenor.com/view/who-who-is-that-guy-toni-collete-knives-out-gif-15093967",
        "https://tenor.com/view/face-pat-patting-face-christopher-plummer-knives-out-gif-15093971",
        "https://tenor.com/view/what-huh-wut-confused-really-gif-15335608",
        "https://tenor.com/view/hmm-think-suspicious-side-eye-lakeith-stanfield-gif-15433720",
        "https://tenor.com/view/drink-sip-hmm-think-suspicious-gif-15433730",
        "https://tenor.com/view/you-may-continue-proceed-keep-going-continue-daniel-craig-gif-15562571",
        "https://tenor.com/view/what-confused-huh-really-shocked-gif-15437123",
        "https://tenor.com/view/dog-german-shepherd-what-pet-doggo-gif-15437126",
        "https://tenor.com/view/whoa-shocked-jaw-drop-wow-really-gif-15437127",
        "https://tenor.com/view/what-huh-confused-really-wut-gif-15437130",
        "https://tenor.com/view/no-nope-nah-idont-think-so-reject-gif-15562567",
        "https://tenor.com/view/you-may-continue-proceed-keep-going-continue-daniel-craig-gif-15562571",
        "https://tenor.com/view/ladies-and-gentlemen-welcome-greet-hello-hi-gif-15562572",
        "https://tenor.com/view/passive-observer-calm-idle-watching-observe-gif-15562569",
        "https://tenor.com/view/eye-roll-toni-collette-knives-out-annoyed-gif-15093963",
        "https://tenor.com/view/wish-birthday-christopher-plummer-knives-out-gif-15093978",
        "https://tenor.com/view/come-on-party-toast-drink-knives-out-gif-15433725",
        "https://tenor.com/view/ransom-yup-yup-knives-out-ransom-d-ransom-drysdale-gif-16881176",
        "https://tenor.com/view/looking-knives-out-daniel-craig-benoit-blanc-gif-16717176",
        "https://tenor.com/view/eat-shit-knives-out-ransom-drysdale-chris-evans-gif-17434928",
        "https://tenor.com/view/no-nope-nah-never-dont-gif-15437132",
        "https://tenor.com/view/chris-evans-knives-out-chrisevans-gif-15826898",
        "https://tenor.com/view/nervous-umm-scared-anxious-marta-gif-14471935",
        "https://tenor.com/view/ana-de-armas-knives-out-drinking-sip-gif-16278294",
        "https://tenor.com/view/toni-collete-knives-out-gif-15433727",
        "https://tenor.com/view/whatever-you-say-bored-chilling-gif-15914282",
        "https://tenor.com/view/conjecture-heavy-duty-chris-evans-knives-out-gif-15094196",
        "https://tenor.com/view/title-intro-magnifying-glass-movie-knives-out-gif-15437122",
        "https://tenor.com/view/giggle-smile-chris-evans-knives-out-gif-15093957",
        "https://tenor.com/view/guilty-guilty-party-daniel-craig-knives-out-gif-15093973",
        "https://tenor.com/view/eating-yummy-cookies-hugry-are-you-talking-to-me-gif-15335612",
        "https://tenor.com/view/oh-it-was-great-awesome-fantastic-amazing-wonderful-gif-14471938"
    ]

    return giflist[yeet]


@bot.event
async def on_ready():
    print("Bot is ready.")


@bot.command(aliases=["Gif"])
async def gif(ctx):
    await ctx.send(randomgif())


bot.run("insert token here")

# sends a random gif from the film Knives Out when requested





