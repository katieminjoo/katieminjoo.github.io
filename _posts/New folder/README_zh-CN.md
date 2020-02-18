# Jekyll Theme Chirpy

[![Build Status](https://github.com/cotes2020/jekyll-theme-chirpy/workflows/build/badge.svg?event=push)](https://github.com/cotes2020/jekyll-theme-chirpy/actions?query=event%3Apush)
[![GitHub license](https://img.shields.io/github/license/cotes2020/jekyll-theme-chirpy.svg)](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/LICENSE)
[![996.icu](https://img.shields.io/badge/link-996.icu-%23FF4D5B.svg)](https://996.icu)

Language: [English](../README.md) | ??ñéÙş

ìé?Üôìé?îÜ Jekyll ñ«?£¨?İ¾ãêİúÍïÎı£©£¬óúéÄ??ãÒ??£¬Û°øµ??¡¢Î·×â¡¢İÂú½?îÜò±?ûú??¡£

**ÍíÒöìé?**

* í»?äŞå¨Ù¼ãÒ
* ÙşíñõÌı¨áóËÇìíÑ¢
* ÙşíñÙÍ?
* í»?õÏ?ßÓ?Ùşíñ
* ?ÛöÍÔÕÕ
* ì£?ÙÍ?
* â¤ßã
* Atom ??
*  Disqus ??
* Google İÂà°
* GA ???Í±£¨ÍÔ?ÍíÒö£©
* SEO ?ûù
* ?ó×àõÒö?ûù

[**î¤???** ¡í](https://chirpy.cotes.info)

![devices-mockup](https://raw.githubusercontent.com/cotes2020/jekyll-theme-chirpy/master/assets/img/sample/devices-mockup.png)

## ÙÍ?

* [äÌ?](#äÌ?)
* [?ú¼ò¦Ñõ](#?ú¼ò¦Ñõ)
* [????](#????)
* [Êï?](#Êï?)
* [?ğ¾](#?ğ¾)
* [?Ê¦??](#?Ê¦??)

## äÌ?

### ñ×?ÍïíÂ

äÎğÎ [Jekyll Î¯Û°Ùş?](https://jekyllrb.com/docs/installation/) èÇà÷Ğñ??ÌÑîÜäÌ? (Ruby£¬RubyGem£¬Bundler ûú Jekyll)¡£?ÖõŞÅéÄ?ÙÍ?Øó?ğ«ÍêîÜÊÅÜâÍïÎı£¬??âÍé©äÌ? [Python](https://www.python.org/downloads/)( >= 3.5) ûú [ruamel.yaml](https://pypi.org/project/ruamel.yaml/)¡£

åıÍı?îÜÏõĞïÍ§?ãÀ Debian ûäíº macOS£¬?âÍé©?ÜÁäÌ?Öõ [GNU coreutils](https://www.gnu.org/software/coreutils/)¡£Üú?£¬÷×?ì¤ù»Û°ãÒ?Ôğ£º

* Debian

 ```console
 $ sudo apt-get install coreutils
 ```

* macOS

 ```console
 $ brew install coreutils
 ```

ïÈó·£¬[fork](https://github.com/cotes2020/jekyll-theme-chirpy/fork) ìé?ÓÛ?£¬æÔı¨Ğº×Ì? Fork îÜ??ÓğÜâò¢ÏõĞïß¾¡£

```console
$ git clone git@github.com:USER/jekyll-theme-chirpy.git
```

`USER` ôğ???îÜ GitHub username¡£



### äÌ? Jekyll ?Ëì

î¤ĞÆÙÍ?ù»?ú¼:

```terminal
$ bundle install
```
`bundle` Ù¤Öµ?í»?äÌ? `Gemfile` ??Ù¥îÜëî??Ëì.



## ?ú¼ò¦Ñõ

### ÙşËìÙÍ?

ù»ØüãÀñ«é©îÜÙşËìÙÍ?£º

```sh
jekyll-theme-chirpy/
¦§¦¡¦¡ _data
¦§¦¡¦¡ _includes      
¦§¦¡¦¡ _layouts
¦§¦¡¦¡ _posts          # posts stay here
¦§¦¡¦¡ _scripts
¦§¦¡¦¡ .travis.yml     # remove it
¦§¦¡¦¡ .github         # remove this, too
¦§¦¡¦¡ assets      
¦§¦¡¦¡ tabs
¦¢   ¦¦¦¡¦¡ about.md    # the ABOUT page
¦§¦¡¦¡ .gitignore
¦§¦¡¦¡ 404.html
¦§¦¡¦¡ Gemfile
¦§¦¡¦¡ LICENSE
¦§¦¡¦¡ README.md
¦§¦¡¦¡ _config.yml     # configuration file
¦§¦¡¦¡ tools           # script tools
¦§¦¡¦¡ docs
¦§¦¡¦¡ feed.xml
¦§¦¡¦¡ index.html
¦§¦¡¦¡ robots.txt
¦¦¦¡¦¡ sitemap.xml
```


?âÍé©?ì¤ù»ÙşËìûäÙÍ??ğ¶:

- .travis.yml
- .github


### ÛÕöÇÙşËì

ĞÆËß?ìÑâÍé©ËÛáóËÇ `_config.yml` îÜ?Õá£¬ÓŞİ»İÂÔ´êóñ¼?Ë¿?éÄÛö¡£

* ?ßÀ
    
    ãÆÖÇîÜ?ßÀÙşËìÛ¯öÇî¤£º`/assets/img/sample/avatar.jpg`. ÷ê??à÷?í»ĞùîÜ?ßÀ£¬ÖØ?ÜôùÚïÒ£¬êÆá³êÆû¿¡£(???ßÀ??Ê¦ß¾???ó×£º*<https://tinypng.com/>* ).

* ??

    ??ë¦ `timezone` ïÒ?£¬Ùù?? `?ñ½/ß¾ú­`£¬åıÍıë¿ãó??é©?àòã¼Ê¦î¤ó®Öªøú?Óğ£º [TimezoneConverter](http://www.timezoneconverter.com/cgi-bin/findzone/findzone) ûäíº [Wikipedia](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).


###  Üâò¢?ú¼

ŞÅéÄì¤ù»ÍïÎıÊ¦?áæ?ú¼:

```terminal
$ bash tools/run.sh
```

??Üâò¢Ü×?£º <http://localhost:4000>

åıÍı?ßÌî¤Üâò¢Ü×??ú¼ı¨£¬÷êáóËÇê¹ÙşËìîÜÌÚËÇ??áìãæ£¬Ê¦ŞÅéÄ?? `-r` (ûä `--realtime`)£¬Üô?é©à»äÌ?ëî? [**fswatch**](http://emcrisostomo.github.io/fswatch/) ¡£

###  İ»ßşÓğ GitHub Pages

İ»ßş?ã·îñ£¬÷ê  `_config.yml` îÜ `url` ËÇ? `https://<username>.github.io`(ûäíº?îÜŞçêóæ´Ù££¬åı£º`https://yourdomain.com`)¡£?èâ£¬åıÍı?ßÌŞÅéÄ [Project ?úş?ó×](https://help.github.com/en/github/working-with-github-pages/about-github-pages#types-of-github-pages-sites)£¬áóËÇÛÕöÇÙşËìîÜ `baseurl` ??ÙÍÙ£?£¬ì¤ŞØ???£¬åı£º`/project`¡£

#### Û°Ûö 1: ë¦ GitHub Pages ßæà÷ó×ïÃ

ëîğÎÜâÛ°Ûö£¬?Ê¦ì¤òÁïÈ÷êê¹?õÏáêÓğ?Ó®??¡£

> **ñ¼**: åıÍı?ßÌŞÅéÄìòù¼Üôî¤??[Öªøú](https://pages.github.com/versions/)ß¾îÜ?Ëì£¬êÆ?ó®Û°Ûö£¬òÁïÈÊ× [*Û°Ûö 2: Üâò¢?Ëï*](#Û°Ûö-2-Üâò¢?Ëï).

**1**. ??ËÇÙ£?:

|ó×ïÃ?úş | ??Ù£?|
|:---|:---|
|User or Organization | `<username>.github.io`|
|Project| `<username>.github.io` ì¤èâîÜÙ£í®£¬Ş§åı `project`|

**2**. ğ«ÎßÜâò¢ÌÚËÇ£¬æÔı¨?ú¼:

```console
$ bash tools/init.sh
```

>**ñ¼**: *õÌı¨ÌÚãæ* ÖªøúĞÆËßÙşíñîÜ git áóËÇ??ßæà÷£¬á¶ì¤?ú¼îñà»÷ê `_posts` ÙÍ?îÜáóËÇğ«Îß¡£

??í»?ßæà÷ÙşíñîÜ *õÌı¨áóËÇìíÑ¢* ûú *İÂ? / ??* ?Øü.

**3**. õÏáêÓğ `origin/master` æÔı¨Óğ GitHub ?????ÙÍ?? Pages Ü×?¡£

**4**. ?ó×??ú¼î¤£º

|ó×ïÃ?úş | ?ó× URL |
|:---|:---|
|User or Organization | `https://<username>.github.io/`|
|Project| `https://<username>.github.io/project/`|


#### Û°Ûö 2: Üâò¢?Ëï

ë¦éÍäÌîïê«ì×£¬GitHub Pages ÜôëÃ?ğ¯ß²Û°?Ëì?ú¼£¬åıÍı?ßÌÔÍ÷ò??£¬ö¦é©Üâò¢?Ëïó×ïÃ?é»¡£

**1**. Óğ GitHub ??£¬?Ëïìé?ãæîÜ??£¬ĞÆËßì¤ù»??Ù¤Ù£: 

|ó×ïÃ?úş | ??Ù£?|
|:---|:---|
|User or Organization | `<username>.github.io`|
|Project| `<username>.github.io` ì¤èâîÜÙ£í®£¬ ÖÇåı `project`|

æÔı¨ Clone ãæ??ÓğÜâò¢¡£

**2**. ?Ëïó×ïÃ:

```console
$ bash tools/build.sh -d /path/to/local/project/
```
> `project` ?ãæ??Ù£?¡£

ßæà÷îÜ??ÙşËì??î¤ `/path/to/local/project`. ÷êãæ??îÜáóËÇğ«Îß?õÏáêÓğ?Ó® `master` İÂò¨.

**3**. üŞÓğ GithHub ??£¬?????? Pages Ü×?¡£

**4**. ?ó×??ú¼î¤:

|ó×ïÃ?úş | ó×ïÃ URL |
|:---|:---|
|User or Organization | `https://<username>.github.io/`|
|Project| `https://<username>.github.io/project/`|


### Ùş?

ÌÚÒı??ĞàÌÚÊ¢îÜ????£¬??? [?ß¾?ïï](https://chirpy.cotes.info/categories/tutorial/)¡£ ?ó®ÔÒ?£¬[Wiki](https://github.com/cotes2020/jekyll-theme-chirpy/wiki) å¥êóìé??ïïîÜÍ¸?¡£


## ????

ß²ìÑú¼ù±êóä²?£¬?çÊğ«?Í± bug, ?ğ¾ËÇ?ÓÛ??Õá£¬ûäíºğ«ÎßãæÍíÒö¡£Îı?ğÃíÂ????ÍÅ[ó®Ùş](.github/CONTRIBUTING.md)£¬????¡£

## Êï?

??ñ«?îÜ??ñ«é©ĞñéÍ [Jekyll](https://jekyllrb.com/) ßæ?¡¢[Bootstrap](https://getbootstrap.com/)¡¢[Font Awesome](https://fontawesome.com/) ûúĞìöâìéŞÁõóßäîÜÍïÎı (ßÓ?ÙşËìñéÊ¦ì¤?Óğ?ŞÁÍïÎıîÜ÷ú?ãáãÓ).

:tada:Êï?á¶êó??ÓÛ???îÜá³?Úá, öâ?îÜ GayHub ID î¤??[Öªøú](https://github.com/cotes2020/jekyll-theme-chirpy/graphs/contributors)¡£ ?èâ, ğ«Îß? issues(ûäíºÚ±ù¬ùê? PR)îÜÍÔİ£?ûúÛÜİ£Ú¸å¥Üô?ù¬?ØÎ,öâ/???ğ¾?Í± bug¡¢İÂú½ãæïÃí­ûäíº??Öõä²?õóÌÚ÷×áÔæ¶?îÜÙş?¡£



## ?ğ¾

åıÍı?ıì???ñ«?ûäíº???êó?ğ¾£¬?ÍÅ?öè?íÂíº£ºî¤ [?ÙÍñ«?](https://github.com/cotes2020/jekyll-theme-chirpy) ïÃ?äÎ? <kbd>:heart:Sponsor</kbd> ??ÎÁùêîÜ?ïÈ?Ê¦èÇà÷£¨??ìéÚõ?ğ¯ì£??ïÈ£¬ò¨Üõ?/Ú°ãá?ğ¾£©£¬?îÜöè????ÓŞò¢ÍÕ?íÂíº£¬??ğ¾íÂíºÌÚû¿ò¢???ÙÍ£¡


## ?Ê¦??

Üâ?ÙÍ?ê¹£¬ĞñéÍ [MIT](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/LICENSE) ?Ê¦¡£