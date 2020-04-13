# -*- coding: UTF-8 -*-
# from django.conf import settings

# python2/3
# git clone https://github.com/python-ldap/python-ldap
# pip3 install python-ldap

import sys
import ldap
import os
import configparser


config = configparser.ConfigParser()
config.read('ldap.conf')
config.sections()

hostargs = os.environ.get("LDAP_HOST")
if hostargs is None:
    hostargs = config['ldap']['LDAP_HOST']
    userargs = config['ldap']['LDAP_ADMIN_USER']
    passwdargs = config['ldap']['LDAP_PASSWORD']
else:
    userargs = os.environ.get("LDAP_ADMIN_USER")
    passwdargs = os.environ.get("LDAP_PASSWORD")

userlist = userargs.split(".")
LDAP_HOST = 'ldap://%s' % hostargs   # LDAP_HOST = 'ldap://172.16.140.118'
USER = 'cn=%s,dc=%s,dc=%s' % (userlist[0], userlist[1], userlist[2])
PASSWORD = passwdargs
BASE_DN = "dc=%s,dc=%s" % (userlist[1], userlist[2])


class LDAP(object):
    def __init__(self, ldap_host=None, base_dn=None, user=None, password=None):
        if not ldap_host:
            ldap_host = LDAP_HOST
        if not base_dn:
            self.base_dn = BASE_DN
        if not user:
            self.user = USER
        if not password:
            self.password = PASSWORD
        try:
            ldap.set_option(ldap.OPT_PROTOCOL_VERSION, ldap.VERSION3)
            self.ldapconn = ldap.initialize(ldap_host)
            self.ldapconn.simple_bind_s(self.user, self.password)
        except ldap.LDAPError as e:
            return e
        except ldap.INVALID_CREDENTIALS as e:
            return (str(e))

    def ldap_get_vaild(self, uid=None, passwd=None):
        target_cn = self.ldap_search_dn(uid)
        try:
            print('target_cn: %s' % target_cn)
            self.ldapconn.simple_bind_s(target_cn, passwd)
        except ldap.INVALID_CREDENTIALS as e:
            return ('ldap_get_vaild user: %s %s' % (uid, e))
        except Exception as e:
            return ('ldap_get_vaild user: %s %s' % (uid, e))
        else:
            return ('user:%s check vaild success' % uid)
        return False

    def ldap_search_dn(self, uid=None):
        searchScope = ldap.SCOPE_SUBTREE
        retrieveAttributes = None
        searchFilter = "uid=" + uid
        try:
            self.ldapconn.simple_bind_s(self.user, self.password)
            print('LDAP connect success!')
            ldap_result_id = self.ldapconn.search(self.base_dn, searchScope, searchFilter, retrieveAttributes)
            result_type, result_data = self.ldapconn.result(ldap_result_id, 0)

            if result_type == ldap.RES_SEARCH_ENTRY:
                # dn = result[0][0]
                return result_data[0][0]
        except ldap.LDAPError as e:
            return ('ldap_search_dn user: %s %s' % (uid, e))
        except Exception as e:
            return ('ldap_get_vaild user: %s %s' % (uid, e))

    # 修改用户密码
    def ldap_update_pass(self, uid=None, oldpass=None, newpass=None):
        target_cn = self.ldap_search_dn(uid)
        try:
            try:
                # 需要绑定manager才有权限改密码
                self.ldapconn.simple_bind_s(self.user, self.password)
                self.ldapconn.passwd_s(target_cn, oldpass, newpass)
                print ('user: %s modify passwd success' % uid)
                return ('user: %s modify passwd success' % uid)
            except ldap.LDAPError as e:
                return ('user: %s %s' % (uid, e))
                return False
        except Exception as e:
            return ('ldap_update_pass: %s %s' % (uid, e))


if __name__ == '__main__':
    ldap_obj = LDAP()

    if len(sys.argv) == 3:
        res = ldap_obj.ldap_get_vaild(sys.argv[1], sys.argv[2])
        print(res)
    if len(sys.argv) == 4:
        res = ldap_obj.ldap_update_pass(sys.argv[1], sys.argv[2], sys.argv[3])
        print(res)
    sys.exit(1)
