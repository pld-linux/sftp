Summary:	sftp: a ftp-replacement over an rsh/ssh tunnel
Summary(pl):	Zamiennik ftp dzia³aj±cy poprzez tunel rsh/ssh
Name:		sftp
Version:	0.9.8
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://www.xbill.org/sftp/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	readline-devel >= 4.1
BuildRequires:	ncurses-devel >= 5.2
URL:		http://www.xbill.org/sftp/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sftp is an ftp replacement that runs over an ssh tunnel. Two programs
are included - sftp and sftpserv. When sftp is run and a host is
connected to (either by running 'sftp remotehost' or 'open remotehost'
from the sftp prompt), an ssh connection is initiated to the remote
host, and sftpserv is run. From within sftp, all of the normal ftp
commands are present: open, close, get, put, pwd, cd, ls, lcd, quit,
etc. There's also exec, which runs a program on the remote end.

%description -l pl
sftp jest zamiennikiem ftp dzia³aj±cym poprzez tunel ssh. Do³±czone s±
dwa programy - sftp i sftpserv.

%prep
%setup -q
%patch0 -p1

%build
aclocal
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_bindir}/sftp \
   $RPM_BUILD_ROOT%{_bindir}/sftpc
mv $RPM_BUILD_ROOT%{_mandir}/man1/sftp.1 \
   $RPM_BUILD_ROOT%{_mandir}/man1/sftpc.1

gzip -9nf README Changelog

%clean
rm -rf $RPM_BUILD_ROOT 

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
