Summary:	Network analyzer
Summary(pl.UTF-8):	Analizator sieci
Name:		tcpick
Version:	0.2.1
Release:	2
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/tcpick/%{name}-%{version}.tar.gz
# Source0-md5:	bb94f2f9ea81aeb645619fbe9b3b9a29
URL:		http://tcpick.sourceforge.net/
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tcpick is a textmode sniffer libpcap-based that can track tcp streams
and saves the captured data in files or displays them in the terminal.

%description -l pl.UTF-8
tcpick jest sniferem opartym o bibliotekę libpcap. Wykrywa strumienie
tcp i zapisuje zdobyte dane do pliku lub wyświetla je w terminalu.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/it/man8

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT%{_mandir}/man8/tcpick_italian.8 \
   $RPM_BUILD_ROOT%{_mandir}/it/man8/tcpick.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog EXAMPLES README doc/*.html
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/*
%lang(it) %{_mandir}/it/man8/*
