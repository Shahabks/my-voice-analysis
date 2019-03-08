from setuptools import setup

long_description="""## the new revision has got a new script and bugs fixed ## 

My-Voice-Analysis is a Python library for the analysis of voice (simultaneous speech, high entropy) 
without the need of a transcription. It breaks utterances and detects syllable boundaries, fundamental 
frequency contours, and formants. Its built-in functions recognize and measures:
 
1.	gender recognition, 
2.	speech mood (semantic analysis), 
3.	pronunciation posterior score 
4.	articulation-rate, 
5.	speech rate,
6.	filler words, 
7.	f0 statistics.
 
The library was developed based upon the idea introduced by Nivja DeJong and Ton Wempe [1], 
Paul Boersma and David Weenink [2], Carlo Gussenhoven [3], S.M Witt and S.J. Young [4] and 
Yannick Jadoul [5].
 
Peaks in intensity (dB) that are preceded and followed by dips in intensity are considered 
as potential syllable cores. 

My-Voice Analysis is unique in its aim to provide a complete quantitative and analytical way 
to study acoustic features of a speech. Moreover, those features could be analysed further 
by employing Python’s functionality to provide more fascinating insights into speech patterns. 

This library is for Linguists, scientists, developers, speech and language therapy clinics and
researchers. Please note that My-Voice Analysis is currently in initial state though in active 
development. While the amount of functionality that is currently present is not huge, more will 
be added over the next few months.

=============
Installation
=============
my-voice-analysis can be installed like any other Python library, using (a recent version of) 
the Python package manager pip, on Linux, macOS, and Windows:

------------- pip install my-voice-analysis
------------------------------
or, to update your installed version to the latest release:
-------------    pip install -u my-voice-analysis
---------------------------------
NOTE: 
After installing My-Voice-Analysis, copy the file 
-----------------myspsolution.praat from--------------
---------- https://github.com/Shahabks/my-voice-analysis ---- 
and save in the directory where you will save audio files for analysis.

Audio files must be in *.wav format, recorded at 44 kHz sample frame and 16 bits of resolution.

To check how the my-voice-analysis functions behave, please check 
---------------- EXAMPLES.docx on --------
------------- https://github.com/Shahabks/my-voice-analysis.-----

My-Voice-Analysis was developed by MYOLUTION Lab in Japan. It is part of New Generation of Voice
Recognition and Analysis Project in MYSOLUTION Lab. That is planned to rich the functionality of 
My-Voice Analysis by adding more advanced functions.

---------https://shahabks.github.io/Mysolution-Lab-AI/ """
	
	
setup(name='my-voice-analysis',
      version='0.7',
      description='the analysis of voice (simultaneous speech) without the need of a transcription',
	  long_description=long_description,
	  url='https://github.com/Shahabks/my-voice-analysis',
      author='Shahab Sabahi',
      author_email='sabahi.s@mysol-gc.jp',
      license='MIT',
      classifiers=[
		'Intended Audience :: Developers',
		'Intended Audience :: Science/Research',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3.7',
		],
	  keywords='praat speech signal processing phonetics',
	  install_requires=[
		'numpy>=1.15.2',
		'praat-parselmouth>=0.3.2',
		'pandas>=0.23.4',
		'scipy>=1.1.0',
		],
	  packages=['my-voice-analysis'],
      zip_safe=False)
	  
