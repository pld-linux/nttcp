Summary:	Network bandwidth measurement tool
Summary(pl):	Narzêdzie do monitorowania przepustowo¶ci sieci
Name:		nttcp
Version:	1.47
Release:	1
License:	GPL
Group:		Networking
Source0:	http://freeware.sgi.com/source/nttcp/%{name}-%{version}.tar.gz
# Source0-md5:	50f0c405b3fa488f6b00db32bf994a7d
URL:		http://www.leo.org/~elmar/nttcp/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NTTCP is a benchmarking tool for determining TCP and UDP performance
between 2 systems.

%description -l pl
NTTCP jest narzêdziem sprawdzaj±cym wydajno¶æ po³±czeñ TCP i UDP
pomiêdzy dwoma systemami.

%prep
%setup -q

%build
%{__make} \
	ARCH="" \
	CC="%{__cc}" \
	OPT="%{rpmcflags}" \
	LFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install nttcp $RPM_BUILD_ROOT%{_bindir}
install nttcp.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
