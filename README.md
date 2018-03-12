# HelloUtau
"Hello World"-like simplest utau plugin, just to see how it works, or "How to write an utau plugin?"

It's been a long time since I wanted to write an utau plugin, and if I had have such an example, I'd have written some plugin years ago. Actually there's the lack of utau programming tutorials.
Some things which wasn't clear for me, and which I was messing with for a long:
1. Don't use PyQt. When compiled, it never run, and I still dunno why. Use PySide, it's all nice the code is actually the same. I don't get it, to be honest.
2. Use Qt Designer or something like this. It's awesome.
3. An utau plugin runs and gives a path to the temp ust in sys.argv[1], which contains some settings and selected notes with previos and next ones. Ust it's a text file and nothing more. Save changes into it.

And after I found out, I suddenly knew that python is not the best choice for a plugin, but nothing could already stop me.
