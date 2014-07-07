%global cartridgedir %{_libexecdir}/openshift/cartridges/egov

Summary:       Provides e-gov3.0 & Tomcat7.0 support
Name:          openshift-origin-cartridge-egov
Version: 0.0.1.1
Release:       1%{?dist}
Group:         Development/Languages
License:       ASL 2.0
URL:           http://openpaas.cloudsc.kr
Source0:       http://mirror.openshift.com/pub/openshift-origin/source/%{name}/%{name}-%{version}.tar.gz
Requires:      facter
Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util
Requires:      lsof
Requires:      java-1.7.0-openjdk
Requires:      java-1.7.0-openjdk-devel
%if 0%{?rhel}
Requires:      maven3
%endif
%if 0%{?fedora}
Requires:      maven
%endif
BuildRequires: jpackage-utils
BuildArch:     noarch

Obsoletes: openshift-origin-cartridge-tomcat-1.0
Obsoletes: openshift-origin-cartridge-tomcat-2.0

%description
Provides EgovFrameWork Tomcat6.0 and Tomcat7.0 support to OpenShift. (Cartridge Format V2)

%prep
%setup -q

%build
%__rm %{name}.spec

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}

%post
# To modify an alternative you should:
# - remove the previous version if it's no longer valid
# - install the new version with an increased priority
# - set the new version as the default to be safe

%if 0%{?rhel}
alternatives --install /etc/alternatives/maven-3.0 maven-3.0 /usr/share/java/apache-maven-3.0.3 100
alternatives --set maven-3.0 /usr/share/java/apache-maven-3.0.3
%endif

%if 0%{?fedora}
alternatives --remove maven-3.0 /usr/share/java/apache-maven-3.0.3
alternatives --install /etc/alternatives/maven-3.0 maven-3.0 /usr/share/maven 102
alternatives --set maven-3.0 /usr/share/maven
%endif

alternatives --remove tomcat-1.0 /usr/share/tomcat6
alternatives --install /etc/alternatives/tomcat-1.0 tomcat-1.0 /usr/share/tomcat6 102
alternatives --set tomcat-1.0 /usr/share/tomcat6

alternatives --remove tomcat-2.0 /usr/share/tomcat7
alternatives --install /etc/alternatives/tomcat-2.0 tomcat-2.0 /usr/share/tomcat7 102
alternatives --set tomcat-2.0 /usr/share/tomcat7

%files
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%{cartridgedir}
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE

%changelog
* Mon July 7 2014 Filirom1 <kikimans@gmail.com> 0.0.1.1
- egov framework create(kikimans@gmail.com)