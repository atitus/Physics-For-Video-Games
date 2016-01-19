\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{tituslab}

\LoadClass[10pt]{book}


\RequirePackage{makeidx,wrapfig,fancyhdr,calc,titlesec,titletoc,amssymb,moreverb,ifthen,color,lmmath}
\RequirePackage[leqno]{amsmath}
%\RequirePackage[sf]{subfigure}%needs to be before caption2
%\RequirePackage[small,sf,nooneline]{caption2}
%   ... This only seems to affect "Figure 1.1," etc., not the actual caption.
%	If I change this style, I need to change my own macros for figures as well.


\definecolor{shadecolor}{gray}{.85} % for framed.sty

\newcommand{\hvsafety}{Do the high voltage safety checklist, Appendix \ref{appendix:hvsafety},
tear it out, and turn it in at the beginning of lab.
If you don't understand
something, don't initial that point, and ask your instructor for clarification before you start the lab.}
\newcommand{\lasersafety}{Do the laser safety checklist, Appendix \ref{appendix:lasersafety},
tear it out, and turn it in at the beginning of lab.
If you don't understand
something, don't initial that point, and ask your instructor for clarification before you start the lab.}
%========================= vectors in bold =========================
% The following is set up so vectors are in upright bold. If I even change my mind and want them in
% slanted bold, it should be easy to change here.
\newcommand{\vc}[1]{\zb{#1}}
%========================= Helvetica for sans serif =========================
\DeclareMathAlphabet{\ms}{OT1}{phv}{m}{sl}
\renewcommand{\sfdefault}{phv} 

%========================= sans serif math stuff =========================
% The following makes use of mixmath.sty, which is my name for some prerelease code
% that Donald Arseneau sent me to allow sans serif and serif math to be mixed in the
% same document gracefully. Once the real package is released, these two macros
% can be rewritten.
\newcommand{\lmsansmath}{\sansmath}
\newcommand{\lmserifmath}{\mathversion{normal}\everymath{}\everydisplay{}}

%========================= design =========================
%chapter: each lab is one
%section: Setup, Observations, ...
%subsection: Used for labs that have parts A, B, ...

%-------------------- sectioning and counters -------------------

%Some magic courtesy of Robin Fairbairns:
\newcommand{\startchaptersonleftpage}{%
	\renewcommand\cleardoublepage{\clearpage
	  \if@twoside
		\ifodd\c@page
		  \hbox{}\newpage
		  \if@twocolumn \hbox{}\newpage \fi
		\fi
	  \fi
	}
}


% Force it to start figure numbering afresh with each section:
\newcommand{\zapcounters}{\setcounter{figure}{0}}
\newcommand{\mychapter}[1]{\zapcounters\chapter{#1}\myeqnspacing}
\newcommand{\mysubsection}[1]{\subsection{#1}}
\newcommand{\mysubsubsection}[1]{\vspace{1 em}{\textsl{#1}}\normalfont\normalsize\\*}

\renewcommand{\thesubsection}{\Alph{labpartctr}}


\definecolor{mygray}{gray}{.55}
%\newcommand{\showingray}[1]{\color{mygray}#1} %----------- causes errors in AR 5.0????
\newcommand{\showingray}[1]{#1}
% titlesec stuff:
\titleformat{\chapter}
  {\normalfont\huge\bfseries\sffamily}{\textit{\thechapter}\qquad}{0mm}{\huge}
\titleformat{\section}
  {\normalfont\Large\bfseries\sffamily}{}{0em}{}
\titleformat{\subsection}
  {\normalfont\normalsize\bfseries\sffamily\refstepcounter{labpartctr}}{\thesubsection}{0.6em}{}
\titleformat{\subsubsection}
  {\normalfont\normalsize\textsl}{\thesubsubsection}{1em}{}

\newcommand{\formatlikechapter}[1]{\normalfont\huge\bfseries\sffamily #1\normalfont\normalsize\\}

\titlespacing*{\chapter}{0mm}{4mm}{6mm}
\titlespacing*{\section}{0mm}{4mm}{0mm} 
\titlespacing{\subsection}{0mm}{1mm}{-0.5mm} 
\titlespacing{\subsubsection}{0mm}{1mm}{-0.5mm} 


\newcounter{prelabctr}[chapter]
\newcounter{labpartctr}[chapter]
\newcounter{appendixctr}

\setcounter{tocdepth}{0}
\setcounter{secnumdepth}{3}

\newcommand{\lab}[1]{\mychapter{#1}}
\newcommand{\labpart}[1]{\subsection{#1}}
\newcommand{\apparatus}{\section*{Apparatus}}
\newcommand{\apparatusdots}{\dotfill}
\newcommand{\equip}[1]{#1\\}
\newcommand{\equipn}[2]{#1 \apparatusdots #2\\}
\newcommand{\introduction}{\section*{Introduction}}
\newcommand{\setup}{\section*{Setup}}
\newcommand{\observations}{\section*{Observations}}
\newcommand{\procedure}{\section*{Procedure}}
\newcommand{\analysis}{\section*{Analysis}}
\newcommand{\results}{\section*{Results}}
\newcommand{\extension}{\section*{Further Investigation}}
\newcommand{\prelab}{\section*{Prelab} The point of the prelab questions is to make sure you understand what you're doing, why you're doing it,
and how to avoid some common mistakes. If you don't know the answers, make sure to come to my office hours before lab and get help! Otherwise you're
just setting yourself up for failure in lab.}
\newcommand{\selfcheck}{\section*{Self-Check}}
\newenvironment{goals}{\section*{Goals}\begin{itemize}}{\end{itemize}}
\newcommand{\goal}[1]{\section*{Goal}#1}
\newcommand{\longgoal}[1]{\section*{Goal}}
\newcommand{\prelabquestion}{\refstepcounter{prelabctr}\noindent\textbf{P\theprelabctr}\quad }
\newlength{\egindent}
\setlength{\egindent}{3mm}
\newlength{\saveleftskip}
\newenvironment{eg}[1]{%
	  	\setlength{\saveleftskip}{\leftskip}%
  		\addtolength{\leftskip}{\egindent}%
  		\small\sffamily
                \emph{Example: #1}\\*\noindent\myeqnspacing\protect\sansmath%
}{\lmserifmath\par\setlength{\leftskip}{\saveleftskip}\par}

\newcommand{\myappendix}[2]{%
  \refstepcounter{appendixctr}%
  \label{appendix:#1}%
  \noindent\chapter{Appendix \ref{appendix:#1}: #2}%
}

\newcommand{\formatappendixtoc}{%
	\renewcommand{\thechapter}{}
}


%-------------------- page layout dimensions -------------------
% standard stuff, see LaTeX companion, p. 85:
  \setlength{\hoffset}{0mm}
  \setlength{\textwidth}{165mm}
  \setlength{\marginparsep}{6mm}
  \setlength{\columnsep}{6mm}
  \setlength{\voffset}{-4mm}
  \setlength{\textheight}{230mm}
  \setlength{\topmargin}{-12mm}
  \setlength{\headheight}{4mm}
  \setlength{\headsep}{8mm}
  \setlength{\footskip}{15mm}
  \setlength{\marginparwidth}{0mm}
  \setlength{\evensidemargin}{0mm}
%-------------------- paragraph formatting -------------------
%Have to do the following /after/ the toc:
\newcommand{\parafmt}{
	\newlength{\normalparindent}% ...has to be after TOC to avoid extra spacing in TOC
	\setlength{\normalparindent}{0mm}
	\setlength{\parindent}{\normalparindent}
	\setlength{\parskip}{2mm}
}
%-------------------- fancyhdr -------------------
\newcommand{\yesiwantarabic}{\renewcommand{\thepage}{\arabic{page}}}
\renewcommand{\headrulewidth}{0mm}
\renewcommand{\footrulewidth}{0mm}
%\setlength{\headrulewidth}{0mm}
\newlength{\myfooterspace}
\setlength{\myfooterspace}{5mm}
\newlength{\myfooterspacep}
\setlength{\myfooterspacep}{19mm}
\pagestyle{fancy}
\renewcommand{\chaptermark}[1]%
  {\markboth{\textsf{\showingray{Chapter\ \thechapter}}\textsf{\hspace{\myfooterspace}#1}}{}}
%\renewcommand{\sectionmark}[1]%
%  {\markright{\textsf{\showingray{Lab\ \thechapter}}\textsf{\hspace{\myfooterspace}#1}}{}}
\renewcommand{\sectionmark}[1]%
  {}
\lhead[]{}
\chead[]{}
\rhead[]{}
\lfoot[\textbf{\textsf{\thepage}} \hspace{\myfooterspacep} \nouppercase{\textsf{\leftmark}}]{}
\cfoot[]{}
\rfoot[]{\nouppercase{\textsf{\rightmark}} \hspace{\myfooterspacep} \textbf{\textsf{\thepage}}}

\fancypagestyle{plain}{% Don't treat 1st page of chapter (lab) any different from others.
}



%-------------------- figure preferences -------------------
% The following three numbers are to make TeX more likely to put figures on the
% same page rather than on a separate figures page. Can tinker with these, but
% make sure floatpagefraction<topfraction.
% Values recommended by the web page I found were 0.85, 0.1, 0.75
%\renewcommand{\topfraction}{0.99}
%\renewcommand{\textfraction}{0.01}
%\renewcommand{\floatpagefraction}{0.98}


%-------------------- my figure commands -------------------
% Letters for figure number, and no "Figure .." in caption:
%  \renewcommand{\figurename}{}
    %...captionlabeldelim: see caption2.sty
%  \def\fnum@figure{\figurename\renewcommand{\captionlabeldelim}{}}
\newcommand{\figinsidetext}[1]{%
  \includegraphics{#1}%
}
\newcommand{\fig}[2][h]{ %
	\begin{figure}[#1]%
	\includegraphics{#2} %
	%\label{fig:#2} %
	\end{figure}%
}
\newcommand{\centerfig}[2][h]{ %
	\begin{figure}[#1]%
	\begin{center}
	\includegraphics{#2} %
	%\label{fig:#2} %
	\end{center}
	\end{figure}%
}
\newcommand{\fignofloat}[1]{%
    \includegraphics{#1}}
%Don't use wide fig without caption, because it gets orphaned.
\newcommand{\widefigcaption}[3][h]{ %
	\begin{figure*}[#1]%
	\includegraphics{#2} %
	\docaption{#3} %
	%\label{fig:#2} %
	\end{figure*}%
}
\newcommand{\figcaptionresize}[3][h]{ %
	\begin{figure}[#1]%
	\includegraphics[width=\columnwidth]{#2} %
	\docaption{#3} %
	%\label{fig:#2} %
	\end{figure}%
}
\newcommand{\figcaption}[3][h]{ %
	\begin{figure}[#1]%
	\includegraphics{#2} %
	\noindent\docaption{#3} %
	%\label{fig:#2} %
	\end{figure}%
}
\newcommand{\docaption}[1]{ %
	\caption{\small{\lmsansmath\sf{#1}\lmserifmath}} %
}

\newcommand{\spacebetweenfigs}{
	\vspace{6mm}
}
%\renewcommand{\thesubfigure}{\footnotesize{subfigure}.\ }
%=========================
\newcommand{\mynormaltype}{\normalsize\normalfont\myeqnspacing}
\newcommand{\myeqnspacing}{
	\setlength{\abovedisplayskip}{4mm plus 1mm minus 3mm}
	\setlength{\belowdisplayskip}{4mm plus 1mm minus 3mm}
	\setlength{\abovedisplayshortskip}{0mm plus 1mm}
	\setlength{\belowdisplayshortskip}{2mm plus 1mm minus 1mm}
}
%==============================toc==================================
% Had problems with hw section entries in toc. They get pushed to the left as a side-
% effect of not numbering them. Decided just to leave them out of toc.
%\newcommand{\formatchtoc}[3]{%
%  \titlecontents{chapter}[0mm]{\addvspace{#3}\sffamily}%
%	{\contentsmargin{0mm}#1\thecontentslabel\enspace#1}%
%	{\contentsmargin{0mm}#1}{#2}[]%
%}
%  \titlecontents{chapter}[0mm]{}%
%	{\contentsmargin{0mm}\large\thecontentslabel\enspace\large}%
%	{\contentsmargin{0mm}\large}{\titlerule*[1pc]{.}\contentspage}[]%
%\contentsmargin{6mm}
\titlecontents{chapter}[1.5em]{}%
	{\contentslabel{2.3em}}%
	{\hspace*{-2.3em}}%
	{\titlerule*[1pc]{.}\contentspage}%
%========================= graphicx package=========================
\newif\ifpdf
\ifx\pdfoutput\undefined
\pdffalse % we are not running PDFLaTeX
\else
\pdfoutput=1 % we are running PDFLaTeX
\pdftrue
\fi

\ifpdf
\usepackage[pdftex]{graphicx}
\else
\usepackage{graphicx}
\fi
%========================= AtBeginDocument stuff=========================
\AtBeginDocument{
  %------------------------------- pdf stuff
	\ifpdf
	\DeclareGraphicsExtensions{.pdf,.jpg,.png}
	\else
	\DeclareGraphicsExtensions{.eps,.jpg,.png}
	\fi
  \newcommand{\chapdir}{glub}
  %------------------------------- equation spacing 
  \myeqnspacing
  	% This gets reset any time I do normalsize, so have to do it after preamble,
  	% and have to use \mynormaltype rather than \normalsize
}
