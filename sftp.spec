Summary:	sftp: a ftp-replacement over an rsh/ssh tunnel
Name:		sftp
Version:	0.9.4
Release:	1
License:	GPL
Group:		Applications/Networking
Group(pl):	Aplikacje/Sieciowe
Source0:	http://www.xbill.org/sftp/download/%{name}-%{version}.tar.gz
Patch0:		sftp-DESTDIR.patch
Patch1:		sftp-LDFLAGS.patch
BuildRequires:	readline-devel >= 4.1
BuildRequires:	ncurses-devel >= 5.0
URL:		http://www.xbill.org/sftp/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sftp is an ftp replacement that runs over an ssh tunnel. Two programs are
included - sftp and sftpserv. When sftp is run and a host is connected to
(either by running 'sftp remotehost' or 'open remotehost' from the sftp
prompt), an ssh connection is initiated to the remote host, and sftpserv is
run. From within sftp, all of the normal ftp commands are present: open,
close, get, put, pwd, cd, ls, lcd, quit, etc. There's also exec, which runs
a program on the remote end.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
LDFLAGS="-s"; export LDFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf README Changelog \
	$RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT 

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
