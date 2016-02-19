%global pkg_name exec-maven-plugin
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        1.2.1
Release:        13.10%{?dist}
Summary:        Exec Maven Plugin

# Most of the files are under ASL 2.0 license, but there are some files
# with no license specified. The project contains MIT license text,
# but there is no file which uses such a license.
License:        ASL 2.0 and MIT
URL:            http://mojo.codehaus.org/exec-maven-plugin
Source0:        http://repo1.maven.org/maven2/org/codehaus/mojo/exec-maven-plugin/1.2.1/exec-maven-plugin-1.2.1-source-release.zip
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch

BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  maven30-maven-invoker-plugin
BuildRequires:  maven30-apache-commons-exec


%description
A plugin to allow execution of system and Java programs

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.


%prep
%setup -q -n exec-maven-plugin-%{version}
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x

sed -i 's/\r$//' LICENSE.txt
find . -name *.jar -delete

cp -p %{SOURCE1} .

%pom_add_dep org.apache.maven:maven-compat pom.xml
%pom_remove_plugin :animal-sniffer-maven-plugin pom.xml
%{?scl:EOF}

%build
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
# There are missing dependencies for tests
%mvn_build -f
%{?scl:EOF}

%install
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE.txt LICENSE-2.0.txt
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt LICENSE-2.0.txt

%changelog
* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 1.2.1-13.10
- maven33 rebuild

* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-13.9
- Add directory ownership on %%{_mavenpomdir} subdir

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.2.1-13.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.2.1-13.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-13.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-13.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-13.4
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Michal Srb <msrb@redhat.com> - 1.2.1-13.3
- SCL-ize BR

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-13.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-13.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.2.1-13
- Mass rebuild 2013-12-27

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-12
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Wed Jun  5 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.2.1-11
- Clean up BuildRequires

* Thu Feb 14 2013 Michal Srb <msrb@redhat.com> - 1.2.1-10
- Disable animal-sniffer plugin

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.2.1-8
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Jan 11 2013 Michal Srb <msrb@redhat.com> - 1.2.1-7
- Fixed rpmlint warnings
- Remove bundled JAR files before building the package

* Wed Jan 09 2013 Michal Srb <msrb@redhat.com> - 1.2.1-6
- maven-plugin-exec renamed (Resolves: #893451)
- Migrated to xmvn

* Wed Nov 28 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-5
- Fix license tag
- Install license files
- Resolves: rhbz#880290

* Wed Nov 28 2012 Tomas Radej <tradej@redhat.com> - 1.2.1-4
- Removed (B)R on plexus-container-default

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 6 2011 Alexander Kurtakov <akurtako@redhat.com> 1.2.1-1
- Update to latest upstream.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Sep 11 2009 Alexander Kurtakov <akurtako@gmail.com> 1.1-1
- Initial package.
