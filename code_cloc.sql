SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS `code_cloc`;
CREATE TABLE `code_cloc` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `createdtime` datetime NOT NULL,
  `lang` varchar(128) NOT NULL,
  `files` int(11) NOT NULL,
  `lines` int(11) NOT NULL,
  `label` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;