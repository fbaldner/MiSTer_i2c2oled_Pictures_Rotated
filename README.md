# MiSTer_i2c2oled_Pictures_Rotated ↪️🖼️
Current release: v0.1

## Premise
If you use [venice's MiSTer_i2c2oled](https://github.com/venice1200/MiSTer_i2c2oled), use your OLED switch with the `ROTATE` option and your OLED display has 16 yellow lines at the top (well, bottom now, since you rotated it), you may have stumbled upon something like the left side of the following picture:

<img src="/i2c2oled_before_and_after.jpg" width="600">

I did and it kinda bothered me until a friday night I decided to see if it'd be easy to switch some limes up and down.

## And...?
It is easy. The .pix files are pretty much just text files and each line is encased in "...". So, I created a Python script (located in the `Python` folder) to make the OLED display something like the right side of the above picture.

## What does this do?
This script pretty much lists every file (should have made it for .pix files only) from [venice's MiSTer_i2c2oled_Pictures repository](https://github.com/venice1200/MiSTer_i2c2oled_Pictures/tree/main) in the `Pix` folder and changes the first 16 lines to be the last 16 lines of the file, saving them on a `Pix_Rotated` folder.

## How to use
If you download the Pictures repository and unpack the file, it'll have a structure such as:
```
\MiSTer_i2c2oled_Pictures-main
 |---- \.github
 |---- \Pictures
        |---- \Pix
        |---- \Pix_Onecolor
```
Just place `rotate.py` in the `\MiSTer_i2c2oled_Pictures-main` and run it. It'll automatically create a `\MiSTer_i2c2oled_Pictures-main\Pictures\Pix_Rotated` folder from the contents of `\MiSTer_i2c2oled_Pictures-main\Pictures\Pix`

## But I don't have Python
Do not fret!

I have made available all 1005 .pix files from venice's repository already rotated.

They're in a .7z file because I pretty much only use GitHub with the web interface and sure as heck i'm not going to send 1000 files in batches of 100.

It's just a 300+KB file anyway.

Just extract them to your MiSTeR's `/media/fat/i2c2oled/Pix` (I'm quoting venice on this one) folder.

If you already have files there, I'd suggest you back them up first so you can go back in case you're not satisfied with the result.

## Disclaimer
Python version: 3.11.1. But I don't use any outstanding libraries, so I'd say it can work with pretty much any version.

Having said that, use at your own risk. I'm not responsible for any damages.

I used venice's repository downloaded on 2023-12-01.

This code isn't the most efficient one ever. It's a 2am product and it does its job, supposedly.

I tested it with `MENU` and also with `TGFX16` and `xmvsf` cores. Then I went to sleep.

But, apparently all 1005 .pix files from that repository have been properly changed from header to footer.

## Issues? Contact?
If you have any constructive criticism, just open an issue here or contact me over on Discord (username is `mechafelipe`).

## Acknowledgements
sorgelig for the [MiSTer](https://github.com/MiSTer-devel)!

venice for [i2c2oled](https://github.com/venice1200/MiSTer_i2c2oled) and the [pix repository](https://github.com/venice1200/MiSTer_i2c2oled_Pictures/tree/main)!

## Changelod
v0.1 @ 2023-12-02: Repository created and everything uploaded
