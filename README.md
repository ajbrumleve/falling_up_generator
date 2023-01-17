<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">Lyrics Generator</h3>

  <p align="center">
    Generate lyrics in the style of your favorite artists
    <br />
    <a href="https://github.com/ajbrumleve/lyrics_generator/issues">Report Bug</a>
    ·
    <a href="https://github.com/ajbrumleve/lyrics_generator/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

This project started as an Udemy project in the course Data Science: Natural Language Processing (NLP) in Python by Lazy Programmer. The original project was to be able to generate poetry by Robert Frost using a second order Markov model. I adapted the project and implemented the Genius API to be able to enter any combination of artists and train a second order Markov model to generate lyrics in the style of those artists.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [![Python][Python]][Python-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started



### Prerequisites

`lyricsgenius` requires Python 3.

Use `pip` to install the package from PyPI:

```bash
pip install lyricsgenius
```

Or, install the latest version of the package from GitHub:

```bash
pip install git+https://github.com/johnwmillr/LyricsGenius.git
```

### Installation



1. Before using this package you'll need to sign up for a (free) account that authorizes access to [the Genius API](http://genius.com/api-clients). The Genius account provides a `access_token` that is required by the package.
2. Clone the repo
   ```sh
   git clone https://github.com/ajbrumleve/lyrics_generator.git
   ```
3. Enter your API in `config.py`
   ```python
   GENIUS_TOKEN = 'ENTER YOUR API'
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Right now, when you run main.py, you are asked for an artist's name. You can then add multiple other artists as well. Once the scrape is done, the .txt file with the artist's lyrics is found in the lyrics folder. Future runs won't have to scrape again. It is important when you enter an artists name that the spelling matches the file name if it exists in the lyrics folder. For example if the file 'lyrics/The Oh Hellos.txt' exists, the artist's name must be enetered as The Oh Hellos and not Oh Hellos. Once the scraping is done, you can choose how many lines of text to generate. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Andrew Brumleve - [@yAndrewBrumleve](https://twitter.com/AndrewBrumleve) - ajbrumleve@gmail.com

Project Link: [https://github.com/ajbrumleve/lyrics_generator](https://github.com/ajbrumleve/lyrics_generator)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Data Science: Natural Language Processing (NLP) in Python](https://www.udemy.com/course/data-science-natural-language-processing-in-python/)
* [lyricsgenius](https://github.com/johnwmillr/LyricsGenius)
* [README Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/ajbrumleve/lyrics_generator.svg?style=for-the-badge
[contributors-url]: https://github.com/ajbrumleve/lyrics_generator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ajbrumleve/lyrics_generator.svg?style=for-the-badge
[forks-url]: https://github.com/ajbrumleve/lyrics_generator/network/members
[stars-shield]: https://img.shields.io/github/stars/ajbrumleve/lyrics_generator.svg?style=for-the-badge
[stars-url]: https://github.com/ajbrumleve/lyrics_generator/stargazers
[issues-shield]: https://img.shields.io/github/issues/ajbrumleve/lyrics_generator.svg?style=for-the-badge
[issues-url]: https://github.com/ajbrumleve/lyrics_generator/issues
[license-shield]: https://img.shields.io/github/license/ajbrumleve/lyrics_generator.svg?style=for-the-badge
[license-url]: https://github.com/ajbrumleve/lyrics_generator/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: (https://www.linkedin.com/in/andrew-brumleve-574239227/)
[product-screenshot]: images/screenshot.png
[Python]:  	https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://python.org/
