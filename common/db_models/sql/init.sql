/*
Navicat MySQL Data Transfer

Source Server         : docker-mysql
Source Server Version : 50727
Source Host           : localhost:3306
Source Database       : api_manager

Target Server Type    : MYSQL
Target Server Version : 50727
File Encoding         : 65001

Date: 2019-10-07 21:10:48
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for am_app_info
-- ----------------------------
DROP TABLE IF EXISTS `am_app_info`;
CREATE TABLE `am_app_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT '' COMMENT '应用名称',
  `content` text COMMENT '应用说明',
  `create_user_id` int(11) DEFAULT '0' COMMENT '创建人id',
  `update_user_id` int(11) DEFAULT '0' COMMENT '最近更新人id',
  `create_time` int(11) DEFAULT '0' COMMENT '创建时间',
  `update_time` int(11) DEFAULT '0' COMMENT '最近更新时间',
  `app_code` varchar(50) DEFAULT '' COMMENT '应用code',
  `is_del` tinyint(4) DEFAULT '0' COMMENT '是否删除：0，否；1，是',
  `token` char(64) DEFAULT '' COMMENT '应用token',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of am_app_info
-- ----------------------------

-- ----------------------------
-- Table structure for am_env
-- ----------------------------
DROP TABLE IF EXISTS `am_env`;
CREATE TABLE `am_env` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT '' COMMENT '环境名称',
  `is_del` tinyint(4) DEFAULT '0' COMMENT '是否删除：0，否；1，是',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of am_env
-- ----------------------------
INSERT INTO `am_env` VALUES ('1', 'dev', '0');
INSERT INTO `am_env` VALUES ('2', 'sit', '0');
INSERT INTO `am_env` VALUES ('3', 'uat', '0');
INSERT INTO `am_env` VALUES ('4', 'prod', '0');

-- ----------------------------
-- Table structure for am_function
-- ----------------------------
DROP TABLE IF EXISTS `am_function`;
CREATE TABLE `am_function` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `env_id` int(11) DEFAULT '0' COMMENT '环境id',
  `app_id` int(11) DEFAULT '0' COMMENT '应用id',
  `platform_num` mediumint(9) DEFAULT '0' COMMENT '涉及的平台计数',
  `is_grey` tinyint(4) DEFAULT '0' COMMENT '是否灰度路由：0，否；1，是',
  `name` varchar(100) DEFAULT '' COMMENT '路由名称',
  `content` text COMMENT '路由说明',
  `function_name` varchar(255) DEFAULT '' COMMENT '函数名（用于查询）',
  `url` varchar(255) DEFAULT '' COMMENT '返回的路由',
  `is_del` tinyint(4) DEFAULT '0' COMMENT '是否删除：0，否；1，是',
  `create_user_id` int(11) DEFAULT '0' COMMENT '创建人id',
  `create_time` int(11) DEFAULT '0' COMMENT '创建时间',
  `del_time` int(11) DEFAULT '0' COMMENT '失效时间',
  `version` float(4,1) DEFAULT '1.0' COMMENT '版本号',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of am_function
-- ----------------------------

-- ----------------------------
-- Table structure for am_platform
-- ----------------------------
DROP TABLE IF EXISTS `am_platform`;
CREATE TABLE `am_platform` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT '' COMMENT '平台名称',
  `num` mediumint(9) DEFAULT '0' COMMENT '平台序列号',
  `content` text COMMENT '平台说明',
  `is_del` tinyint(4) DEFAULT '0' COMMENT '是否删除：0，否；1，是',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of am_platform
-- ----------------------------

-- ----------------------------
-- Table structure for am_role
-- ----------------------------
DROP TABLE IF EXISTS `am_role`;
CREATE TABLE `am_role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT '' COMMENT '角色名称',
  `content` text COMMENT '角色说明',
  `is_del` tinyint(4) DEFAULT '0' COMMENT '是否删除：0，否；1，是',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of am_role
-- ----------------------------
INSERT INTO `am_role` VALUES ('1', '超级管理员', '超级管理员', '0');
INSERT INTO `am_role` VALUES ('2', '应用管理员', '应用管理员', '0');
INSERT INTO `am_role` VALUES ('3', '普通用户', '普通数据查看用户', '0');

-- ----------------------------
-- Table structure for am_user_info
-- ----------------------------
DROP TABLE IF EXISTS `am_user_info`;
CREATE TABLE `am_user_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) DEFAULT '' COMMENT '用户名',
  `password` char(64) DEFAULT '' COMMENT '用户密码，使用sha256加密',
  `content` text COMMENT '用户说明',
  `role_id` int(11) DEFAULT '0' COMMENT '用户角色',
  `is_del` tinyint(4) DEFAULT '0' COMMENT '是否删除：0，否；1，是',
  `create_user_id` int(11) DEFAULT '0',
  `create_time` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

