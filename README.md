# Common Passwords: A Security Risk Analysis

## Introduction

In the digital era, password security is a fundamental aspect of protecting personal and sensitive information. Despite repeated warnings, many users continue to rely on weak and common passwords, significantly increasing the risk of unauthorized access. This study analyzes a dataset of 7 million passwords obtained from a data breach to identify common passwords and their usage frequencies. The purpose is to highlight the importance of using strong, unique passwords and to provide actionable recommendations for enhancing password security.

## Methodology

A Python script was used to process the dataset, counting the occurrences of each password and calculating their respective percentages. The analysis focused on the second pieces of text in each line, which represented the passwords. The criteria for a strong password were defined as a minimum of 8 characters, containing numbers, uppercase letters, and special characters.

## Results

### Password Analysis:
1. **Longest password:** San**************************z (Length: 30) (was an actual name so I had to anonymize it)
2. **Shortest password:** Nanna (Length: 5)
3. **Average password length:** 9.46
4. **Passwords with special characters:** 637001 (9.10%)
5. **Passwords with numbers:** 5574045 (79.63%)
6. **Strong passwords:** 348758 (4.98%)

### Top 100 Frequent Passwords:
1. 123456 (23049) 0.33% (17.46% of top 100)
2. 123456789 (9261) 0.13% (7.01% of top 100)
3. password (7800) 0.11% (5.91% of top 100)
4. picture1 (6586) 0.09% (4.99% of top 100)
5. 12345678 (6053) 0.09% (4.58% of top 100)
6. unknown (3393) 0.05% (2.57% of top 100)
7. 1234567890 (3112) 0.04% (2.36% of top 100)
8. Password (3077) 0.04% (2.33% of top 100)
9. qwerty (2634) 0.04% (1.99% of top 100)
10. 1234567 (2578) 0.04% (1.95% of top 100)
Complete list below....

### Total Unique Passwords:
5561577

## Discussion

### Risks of Using Common Passwords

Using simple, common passwords poses a significant security risk. Attackers often use techniques such as dictionary attacks, where they try a list of common passwords to gain unauthorized access to accounts. The prevalence of passwords like "password" and "123456" indicates that many users are still not adhering to basic password security practices. 

### Comments and Observations

The most striking observation is the high frequency of extremely simple and predictable passwords, such as "123456" and "password". These passwords are highly vulnerable to brute force attacks. Moreover, the analysis shows that only a small fraction (4.98%) of passwords can be considered strong under the criteria defined, emphasizing the widespread use of weak passwords. 

Interestingly, the analysis also highlights the inclusion of special characters and numbers in passwords, but these elements alone are not sufficient to ensure password strength. The average password length of 9.46 characters suggests that many users are meeting the minimum length requirement for passwords but are not necessarily creating complex and unique passwords.

## Recommendations

1. **Use Strong, Unique Passwords:** Passwords should be long, complex, and unique to each account. A good password might look something like "mY!S3cuR3Pa$$w0rD#2024" instead of "password".

2. **Utilize Password Managers:** Tools like Bitwarden (no affiliation), LastPass, or 1Password can help generate and store strong passwords, making it easier to manage multiple unique passwords.

3. **Enable Two-Factor Authentication (2FA):** Adding an extra layer of security, such as a text message code or an authenticator app, can protect accounts even if the password is compromised.

4. **Check for Breaches:** Users can check if their email addresses have been compromised in data breaches by using services like [Have I Been Pwned](https://haveibeenpwned.com/).

## Conclusion

This analysis underscores the critical need for improved password security practices. By using strong, unique passwords, leveraging password managers, enabling two-factor authentication, and regularly checking for data breaches, users can significantly enhance their online security and reduce the risk of unauthorized access.

## Next Steps

For further analysis, users can find out if their email address has been found in a data breach at [Have I Been Pwned](https://haveibeenpwned.com/). It is also highly recommended to regularly update passwords and follow best practices for online security.


## Complete Top 100 frequent words:
1. 123456 (23049) 0.33% (17.46% of top 100)
2. 123456789 (9261) 0.13% (7.01% of top 100)
3. password (7800) 0.11% (5.91% of top 100)
4. picture1 (6586) 0.09% (4.99% of top 100)
5. 12345678 (6053) 0.09% (4.58% of top 100)
6. unknown (3393) 0.05% (2.57% of top 100)
7. 1234567890 (3112) 0.04% (2.36% of top 100)
8. Password (3077) 0.04% (2.33% of top 100)
9. qwerty (2634) 0.04% (1.99% of top 100)
10. 1234567 (2578) 0.04% (1.95% of top 100)
11. 12345 (2544) 0.04% (1.93% of top 100)
12. 111111 (2400) 0.03% (1.82% of top 100)
13. 123123 (2346) 0.03% (1.78% of top 100)
14. abc123 (2068) 0.03% (1.57% of top 100)
15. vvm2019 (1901) 0.03% (1.44% of top 100)
16. 000000 (1748) 0.02% (1.32% of top 100)
17. (null) (1575) 0.02% (1.19% of top 100)
18. yuantuo2012 (1386) 0.02% (1.05% of top 100)
19. Ghjghjghj9 (1352) 0.02% (1.02% of top 100)
20. iloveyou (1295) 0.02% (0.98% of top 100)
21. password1 (1255) 0.02% (0.95% of top 100)
22. qwerty123 (1101) 0.02% (0.83% of top 100)
23. qwertyuiop (1081) 0.02% (0.82% of top 100)
24. 3Odi15ngxB (1046) 0.01% (0.79% of top 100)
25. princess (1012) 0.01% (0.77% of top 100)
26. 1q2w3e4r (996) 0.01% (0.75% of top 100)
27. dragon (966) 0.01% (0.73% of top 100)
28. sunshine (940) 0.01% (0.71% of top 100)
29. Sojdlg123aljg (907) 0.01% (0.69% of top 100)
30. admin (877) 0.01% (0.66% of top 100)
31. weborder (875) 0.01% (0.66% of top 100)
32. 1q2w3e4r5t (837) 0.01% (0.63% of top 100)
33. monkey (824) 0.01% (0.62% of top 100)
34. 123321 (815) 0.01% (0.62% of top 100)
35. 1qaz2wsx (769) 0.01% (0.58% of top 100)
36. abcd1234 (768) 0.01% (0.58% of top 100)
37. 654321 (717) 0.01% (0.54% of top 100)
38. qwe123 (671) 0.01% (0.51% of top 100)
39. samantha (669) 0.01% (0.51% of top 100)
40. baseball (658) 0.01% (0.50% of top 100)
41. 0r968ji9ufj6 (642) 0.01% (0.49% of top 100)
42. asdfghjkl (608) 0.01% (0.46% of top 100)
43. 76bshv6gdd (591) 0.01% (0.45% of top 100)
44. 123qwe (584) 0.01% (0.44% of top 100)
45. 310909 (582) 0.01% (0.44% of top 100)
46. football (580) 0.01% (0.44% of top 100)
47. minecraft (576) 0.01% (0.44% of top 100)
48. Password1 (575) 0.01% (0.44% of top 100)
49. 987654321 (562) 0.01% (0.43% of top 100)
50. michael (560) 0.01% (0.42% of top 100)
51. passw0rd (554) 0.01% (0.42% of top 100)
52. 12345678910 (544) 0.01% (0.41% of top 100)
53. 1234qwer (529) 0.01% (0.40% of top 100)
54. 666666 (528) 0.01% (0.40% of top 100)
55. password123 (523) 0.01% (0.40% of top 100)
56. zxcvbnm (516) 0.01% (0.39% of top 100)
57. [UNKNOWN (514) 0.01% (0.39% of top 100)
58. A1b2c3 (513) 0.01% (0.39% of top 100)
59. Defaultpassw0rd (505) 0.01% (0.38% of top 100)
60. superman (505) 0.01% (0.38% of top 100)
61. 112233 (500) 0.01% (0.38% of top 100)
62. 123123123 (500) 0.01% (0.38% of top 100)
63. pokemon (483) 0.01% (0.37% of top 100)
64. 121212 (479) 0.01% (0.36% of top 100)
65. michelle (479) 0.01% (0.36% of top 100)
66. shadow (478) 0.01% (0.36% of top 100)
67. defaultPassw0rd (475) 0.01% (0.36% of top 100)
68. asdf1234 (470) 0.01% (0.36% of top 100)
69. defaultpassw0rd (469) 0.01% (0.36% of top 100)
70. qwerty1 (463) 0.01% (0.35% of top 100)
71. 1g2w3e4r (457) 0.01% (0.35% of top 100)
72. qwer1234 (455) 0.01% (0.34% of top 100)
73. trustno1 (452) 0.01% (0.34% of top 100)
74. whatever (443) 0.01% (0.34% of top 100)
75. basketball (438) 0.01% (0.33% of top 100)
76. gwerty (435) 0.01% (0.33% of top 100)
77. q1w2e3r4 (434) 0.01% (0.33% of top 100)
78. Anninau0109@ (433) 0.01% (0.33% of top 100)
79. soccer (430) 0.01% (0.33% of top 100)
80. 0987654321 (418) 0.01% (0.32% of top 100)
81. hello123 (412) 0.01% (0.31% of top 100)
82. 7777777 (410) 0.01% (0.31% of top 100)
83. 159753 (407) 0.01% (0.31% of top 100)
84. d2Xyw89sxJ (402) 0.01% (0.30% of top 100)
85. qwerty12 (401) 0.01% (0.30% of top 100)
86. 321321321 (399) 0.01% (0.30% of top 100)
87. linkedin (399) 0.01% (0.30% of top 100)
88. loseweight (398) 0.01% (0.30% of top 100)
89. welcome (394) 0.01% (0.30% of top 100)
90. 123456a (391) 0.01% (0.30% of top 100)
91. charlie (386) 0.01% (0.29% of top 100)
92. computer (383) 0.01% (0.29% of top 100)
93. jordan23 (382) 0.01% (0.29% of top 100)
94. <password> (381) 0.01% (0.29% of top 100)
95. 123abc (381) 0.01% (0.29% of top 100)
96. Minecraft (379) 0.01% (0.29% of top 100)
97. uQA9Ebw445 (377) 0.01% (0.29% of top 100)
98. 12341234 (376) 0.01% (0.28% of top 100)
99. nicholas (375) 0.01% (0.28% of top 100)
100. andrew (375) 0.01% (0.28% of top 100)
"# Top-100-Passwords-2024" 