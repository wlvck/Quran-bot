from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .callback_datas import name_callback, cancel_callback, go_to

# ------------------------------InlineKeyboardMarkup First Page ------------------------------------------
first_page = InlineKeyboardMarkup(row_width=5,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(
                                              text='1. Алла (Аллаһ)',
                                              callback_data=name_callback.new(greatest_name='1')
                                          )
                                      ],
                                      [
                                          InlineKeyboardButton(
                                              text='2. Ар-Рахмаан',
                                              callback_data=name_callback.new(greatest_name='2')
                                          ),
                                          InlineKeyboardButton(
                                              text='3. Ар-Рахиим',
                                              callback_data=name_callback.new(greatest_name='3')
                                          ),

                                      ],
                                      [
                                          InlineKeyboardButton(
                                              text='4. Әл-Мәлик',
                                              callback_data=name_callback.new(greatest_name='4')
                                          ),
                                          InlineKeyboardButton(
                                              text='5. Әл-Қуддуус',
                                              callback_data=name_callback.new(greatest_name='5')
                                          ),

                                      ],
                                      [
                                          InlineKeyboardButton(
                                              text='6. Әс-Сәләәм',
                                              callback_data=name_callback.new(greatest_name='6')
                                          ),
                                          InlineKeyboardButton(
                                              text='7. Әл-Мумин',
                                              callback_data=name_callback.new(greatest_name='7')
                                          ),

                                      ],
                                      [
                                          InlineKeyboardButton(
                                              text='8. Әл-Муһәймин',
                                              callback_data=name_callback.new(greatest_name='8')
                                          ),
                                          InlineKeyboardButton(
                                              text='9. Әл-Азииз',
                                              callback_data=name_callback.new(greatest_name='9')
                                          ),

                                      ],
                                      [
                                          InlineKeyboardButton(
                                              text='10. Әл-Жаббаар',
                                              callback_data=name_callback.new(greatest_name='10')
                                          ),
                                          InlineKeyboardButton(
                                              text='11. Әл-Мутәкәббир',
                                              callback_data=name_callback.new(greatest_name='11')
                                          )
                                      ],
                                      [
                                          InlineKeyboardButton(
                                              text='•1•',
                                              callback_data=go_to.new(page='page_1')
                                          ),
                                          InlineKeyboardButton(
                                              text='2',
                                              callback_data=go_to.new(page='page_2')
                                          ),
                                          InlineKeyboardButton(
                                              text='3',
                                              callback_data=go_to.new(page='page_3')
                                          ),
                                          InlineKeyboardButton(
                                              text='4 ›',
                                              callback_data=go_to.new(page='page_4')
                                          ),
                                          InlineKeyboardButton(
                                              text='9»',
                                              callback_data=go_to.new(page='page_9')
                                          )
                                      ]
                                  ])

# ------------------------------InlineKeyboardMarkup Second Page ------------------------------------------
second_page = InlineKeyboardMarkup(row_width=5,
                                   inline_keyboard=[
                                       [
                                           InlineKeyboardButton(
                                               text='12. Әл-Хаалиқ',
                                               callback_data=name_callback.new(greatest_name='12')
                                           )
                                       ],
                                       [
                                           InlineKeyboardButton(
                                               text='13. Әл-Баари',
                                               callback_data=name_callback.new(greatest_name='13')
                                           ),
                                           InlineKeyboardButton(
                                               text='14. Әл-Мусаууир',
                                               callback_data=name_callback.new(greatest_name='14')
                                           ),

                                       ],
                                       [
                                           InlineKeyboardButton(
                                               text='15. Әл-Ғаффар',
                                               callback_data=name_callback.new(greatest_name='15')
                                           ),
                                           InlineKeyboardButton(
                                               text='16. Әл-Қаһһар',
                                               callback_data=name_callback.new(greatest_name='16')
                                           ),

                                       ],
                                       [
                                           InlineKeyboardButton(
                                               text='17. Әл-Уаһһаб',
                                               callback_data=name_callback.new(greatest_name='17')
                                           ),
                                           InlineKeyboardButton(
                                               text='18. Ар-Раззақ',
                                               callback_data=name_callback.new(greatest_name='18')
                                           ),

                                       ],
                                       [
                                           InlineKeyboardButton(
                                               text='19. Әл-Фаттах',
                                               callback_data=name_callback.new(greatest_name='19')
                                           ),
                                           InlineKeyboardButton(
                                               text='20. Әл-Алиим',
                                               callback_data=name_callback.new(greatest_name='20')
                                           ),

                                       ],
                                       [
                                           InlineKeyboardButton(
                                               text='21. Әл-Қаабид',
                                               callback_data=name_callback.new(greatest_name='21')
                                           ),
                                           InlineKeyboardButton(
                                               text='22. Әл-Баасит',
                                               callback_data=name_callback.new(greatest_name='22')
                                           )
                                       ],
                                       [
                                           InlineKeyboardButton(
                                               text='1',
                                               callback_data=go_to.new(page='page_1')
                                           ),
                                           InlineKeyboardButton(
                                               text='•2•',
                                               callback_data=go_to.new(page='page_2')
                                           ),
                                           InlineKeyboardButton(
                                               text='3',
                                               callback_data=go_to.new(page='page_3')
                                           ),
                                           InlineKeyboardButton(
                                               text='4 ›',
                                               callback_data=go_to.new(page='page_4')
                                           ),
                                           InlineKeyboardButton(
                                               text='9»',
                                               callback_data=go_to.new(page='page_9')
                                           )
                                       ]
                                   ])

# ------------------------------InlineKeyboardMarkup Third Page ------------------------------------------

third_page = InlineKeyboardMarkup(row_width=5,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(
                                              text='23. Әл-Хаафид',
                                              callback_data=name_callback.new(greatest_name='23')
                                          )
                                      ],
                                      [
                                          InlineKeyboardButton(
                                              text='24. Ар-Раафиъ',
                                              callback_data=name_callback.new(greatest_name='24')
                                          ),
                                          InlineKeyboardButton(
                                              text='25. Әл-Муъиззу',
                                              callback_data=name_callback.new(greatest_name='25')
                                          ),
                                      ],
                                      [
                                          InlineKeyboardButton(
                                              text='26. Әл-Музиллу',
                                              callback_data=name_callback.new(greatest_name='26')
                                          ),
                                          InlineKeyboardButton(
                                              text='27. Әс-Сәмииъу',
                                              callback_data=name_callback.new(greatest_name='27')
                                          ),
                                      ],
                                      [
                                          InlineKeyboardButton(
                                              text='28. Әл-Басиир',
                                              callback_data=name_callback.new(greatest_name='28')
                                          ),
                                          InlineKeyboardButton(
                                              text='29. Әл-Хакам',
                                              callback_data=name_callback.new(greatest_name='29')
                                          ),
                                      ],
                                      [
                                          InlineKeyboardButton(
                                              text='30. Әл-Адл',
                                              callback_data=name_callback.new(greatest_name='30')
                                          ),
                                          InlineKeyboardButton(
                                              text='31. Әл-Латииф',
                                              callback_data=name_callback.new(greatest_name='31')
                                          ),
                                      ],
                                      [
                                          InlineKeyboardButton(
                                              text='32. Әл-Хабиир',
                                              callback_data=name_callback.new(greatest_name='32')
                                          ),
                                          InlineKeyboardButton(
                                              text='33. Әл-Халиим',
                                              callback_data=name_callback.new(greatest_name='33')
                                          )
                                      ],
                                      [
                                          InlineKeyboardButton(
                                              text='1',
                                              callback_data=go_to.new(page='page_1')
                                          ),
                                          InlineKeyboardButton(
                                              text='2',
                                              callback_data=go_to.new(page='page_2')
                                          ),
                                          InlineKeyboardButton(
                                              text='•3•',
                                              callback_data=go_to.new(page='page_3')
                                          ),
                                          InlineKeyboardButton(
                                              text='4 ›',
                                              callback_data=go_to.new(page='page_4')
                                          ),
                                          InlineKeyboardButton(
                                              text='9»',
                                              callback_data=go_to.new(page='page_9')
                                          )
                                      ]
                                  ])

# ------------------------------InlineKeyboardMarkup Fourth Page ------------------------------------------

fourth_page = InlineKeyboardMarkup(row_width=5,
                                   inline_keyboard=[
                                       [
                                           InlineKeyboardButton(
                                               text='34. Әл-Азиим ',
                                               callback_data=name_callback.new(greatest_name='34')
                                           )
                                       ],
                                       [
                                           InlineKeyboardButton(
                                               text='35. Әл-Ғафуур',
                                               callback_data=name_callback.new(greatest_name='35')
                                           ),
                                           InlineKeyboardButton(
                                               text='36. Әш-Шәкуур',
                                               callback_data=name_callback.new(greatest_name='36')
                                           ),
                                       ],
                                       [
                                           InlineKeyboardButton(
                                               text='37. Әл-Алий',
                                               callback_data=name_callback.new(greatest_name='37')
                                           ),
                                           InlineKeyboardButton(
                                               text='38. Әл-Кәбиир',
                                               callback_data=name_callback.new(greatest_name='38')
                                           ),
                                       ],
                                       [
                                           InlineKeyboardButton(
                                               text='39. Әл-Хафииз',
                                               callback_data=name_callback.new(greatest_name='39')
                                           ),
                                           InlineKeyboardButton(
                                               text='40. Әл-Муқиит',
                                               callback_data=name_callback.new(greatest_name='40')
                                           ),
                                       ],
                                       [
                                           InlineKeyboardButton(
                                               text='41. Әл-Хасииб',
                                               callback_data=name_callback.new(greatest_name='41')
                                           ),
                                           InlineKeyboardButton(
                                               text='42. Әл-Жәлиил ',
                                               callback_data=name_callback.new(greatest_name='42')
                                           ),
                                       ],
                                       [
                                           InlineKeyboardButton(
                                               text='43. Әл-Кәриим',
                                               callback_data=name_callback.new(greatest_name='43')
                                           ),
                                           InlineKeyboardButton(
                                               text='44. Ар-Рақииб',
                                               callback_data=name_callback.new(greatest_name='44')
                                           )
                                       ],
                                       [
                                           InlineKeyboardButton(
                                               text='«1',
                                               callback_data=go_to.new(page='page_1')
                                           ),
                                           InlineKeyboardButton(
                                               text='‹ 3',
                                               callback_data=go_to.new(page='page_3')
                                           ),
                                           InlineKeyboardButton(
                                               text='•4•',
                                               callback_data=go_to.new(page='page_4')
                                           ),
                                           InlineKeyboardButton(
                                               text='5 ›',
                                               callback_data=go_to.new(page='page_5')
                                           ),
                                           InlineKeyboardButton(
                                               text='9»',
                                               callback_data=go_to.new(page='page_9')
                                           )
                                       ]
                                   ])

# ------------------------------InlineKeyboardMarkup Fifth Page ------------------------------------------

fifth_page = InlineKeyboardMarkup(row_width=5,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(
                                              text='45. Әл-Мужииб ',
                                              callback_data=name_callback.new(greatest_name='45')
                                          )
                                      ],
                                      [
                                          InlineKeyboardButton(
                                              text='46. Әл-Уаасиғ',
                                              callback_data=name_callback.new(greatest_name='46')
                                          ),
                                          InlineKeyboardButton(
                                              text='47. Әл-Хакиим',
                                              callback_data=name_callback.new(greatest_name='47')
                                          ),
                                      ],
                                      [
                                          InlineKeyboardButton(
                                              text='48. Әл-Уадууд',
                                              callback_data=name_callback.new(greatest_name='48')
                                          ),
                                          InlineKeyboardButton(
                                              text='49. Әл-Мәжиид',
                                              callback_data=name_callback.new(greatest_name='49')
                                          ),
                                      ],
                                      [
                                          InlineKeyboardButton(
                                              text='50. Әл-Баағис',
                                              callback_data=name_callback.new(greatest_name='50')
                                          ),
                                          InlineKeyboardButton(
                                              text='51. Әш-Шәһиид',
                                              callback_data=name_callback.new(greatest_name='51')
                                          ),
                                      ],
                                      [
                                          InlineKeyboardButton(
                                              text='52. Әл-Хаққ',
                                              callback_data=name_callback.new(greatest_name='52')
                                          ),
                                          InlineKeyboardButton(
                                              text='53. Әл-Уакиил',
                                              callback_data=name_callback.new(greatest_name='53')
                                          ),
                                      ],
                                      [
                                          InlineKeyboardButton(
                                              text='54. Әл-Қауий',
                                              callback_data=name_callback.new(greatest_name='54')
                                          ),
                                          InlineKeyboardButton(
                                              text='55. Әл-Мәтиин',
                                              callback_data=name_callback.new(greatest_name='55')
                                          )
                                      ],
                                      [
                                          InlineKeyboardButton(
                                              text='«1',
                                              callback_data=go_to.new(page='page_1')
                                          ),
                                          InlineKeyboardButton(
                                              text='‹ 4',
                                              callback_data=go_to.new(page='page_4')
                                          ),
                                          InlineKeyboardButton(
                                              text='•5•',
                                              callback_data=go_to.new(page='page_5')
                                          ),
                                          InlineKeyboardButton(
                                              text='6 ›',
                                              callback_data=go_to.new(page='page_6')
                                          ),
                                          InlineKeyboardButton(
                                              text='9»',
                                              callback_data=go_to.new(page='page_9')
                                          )
                                      ]
                                  ])
# ------------------------------InlineKeyboardMarkup Sixth Page ------------------------------------------

sixth_page = InlineKeyboardMarkup(row_width=5,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(
                                              text='56. Әл-Уалий',
                                              callback_data=name_callback.new(greatest_name='56')
                                          )
                                      ],
                                      [
                                          InlineKeyboardButton(
                                              text='57. Әл-Хамиид',
                                              callback_data=name_callback.new(greatest_name='57')
                                          ),
                                          InlineKeyboardButton(
                                              text='58. Әл-Мухсии',
                                              callback_data=name_callback.new(greatest_name='58')
                                          ),
                                      ],
                                      [
                                          InlineKeyboardButton(
                                              text='59. Әл-Мубдии',
                                              callback_data=name_callback.new(greatest_name='59')
                                          ),
                                          InlineKeyboardButton(
                                              text='60. Әл-Муғиид',
                                              callback_data=name_callback.new(greatest_name='60')
                                          ),
                                      ],
                                      [
                                          InlineKeyboardButton(
                                              text='61. Әл-Мухии',
                                              callback_data=name_callback.new(greatest_name='61')
                                          ),
                                          InlineKeyboardButton(
                                              text='62. Әл-Мумиит',
                                              callback_data=name_callback.new(greatest_name='62')
                                          ),
                                      ],
                                      [
                                          InlineKeyboardButton(
                                              text='63. Әл-Хайй',
                                              callback_data=name_callback.new(greatest_name='63')
                                          ),
                                          InlineKeyboardButton(
                                              text='64. Әл-Қаййум',
                                              callback_data=name_callback.new(greatest_name='64')
                                          ),
                                      ],
                                      [
                                          InlineKeyboardButton(
                                              text='65. Әл-Уаажид',
                                              callback_data=name_callback.new(greatest_name='65')
                                          ),
                                          InlineKeyboardButton(
                                              text='66. Әл-Мәәжид',
                                              callback_data=name_callback.new(greatest_name='66')
                                          )
                                      ],
                                      [
                                          InlineKeyboardButton(
                                              text='«1',
                                              callback_data=go_to.new(page='page_1')
                                          ),
                                          InlineKeyboardButton(
                                              text='‹ 5',
                                              callback_data=go_to.new(page='page_5')
                                          ),
                                          InlineKeyboardButton(
                                              text='•6•',
                                              callback_data=go_to.new(page='page_6')
                                          ),
                                          InlineKeyboardButton(
                                              text='7 ›',
                                              callback_data=go_to.new(page='page_7')
                                          ),
                                          InlineKeyboardButton(
                                              text='9»',
                                              callback_data=go_to.new(page='page_9')
                                          )
                                      ]
                                  ])

# ------------------------------InlineKeyboardMarkup Seventh Page ------------------------------------------

seventh_page = InlineKeyboardMarkup(row_width=5,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(
                                                text='67. Әл-Уаахид',
                                                callback_data=name_callback.new(greatest_name='67')
                                            )
                                        ],
                                        [
                                            InlineKeyboardButton(
                                                text='68. Ас-Самад ',
                                                callback_data=name_callback.new(greatest_name='68')
                                            ),
                                            InlineKeyboardButton(
                                                text='69. Әл-Қаадир',
                                                callback_data=name_callback.new(greatest_name='69')
                                            ),
                                        ],
                                        [
                                            InlineKeyboardButton(
                                                text='70. Әл-Муқтадир',
                                                callback_data=name_callback.new(greatest_name='70')
                                            ),
                                            InlineKeyboardButton(
                                                text='71. Әл-Муқаддим',
                                                callback_data=name_callback.new(greatest_name='71')
                                            ),
                                        ],
                                        [
                                            InlineKeyboardButton(
                                                text='72. Әл-Муаххир',
                                                callback_data=name_callback.new(greatest_name='72')
                                            ),
                                            InlineKeyboardButton(
                                                text='73. Әл-Әууәл',
                                                callback_data=name_callback.new(greatest_name='73')
                                            ),
                                        ],
                                        [
                                            InlineKeyboardButton(
                                                text='74. Әл-Аахир',
                                                callback_data=name_callback.new(greatest_name='74')
                                            ),
                                            InlineKeyboardButton(
                                                text='75. Аз-Зааһир',
                                                callback_data=name_callback.new(greatest_name='75')
                                            ),
                                        ],
                                        [
                                            InlineKeyboardButton(
                                                text='76. Әл-Баатин',
                                                callback_data=name_callback.new(greatest_name='76')
                                            ),
                                            InlineKeyboardButton(
                                                text='77. Әл-Уаали',
                                                callback_data=name_callback.new(greatest_name='77')
                                            )
                                        ],
                                        [
                                            InlineKeyboardButton(
                                                text='«1',
                                                callback_data=go_to.new(page='page_1')
                                            ),
                                            InlineKeyboardButton(
                                                text='‹ 6',
                                                callback_data=go_to.new(page='page_6')
                                            ),
                                            InlineKeyboardButton(
                                                text='•7•',
                                                callback_data=go_to.new(page='page_7')
                                            ),
                                            InlineKeyboardButton(
                                                text='8',
                                                callback_data=go_to.new(page='page_8')
                                            ),
                                            InlineKeyboardButton(
                                                text='9',
                                                callback_data=go_to.new(page='page_9')
                                            )
                                        ]
                                    ])

# ------------------------------InlineKeyboardMarkup Eighth Page ------------------------------------------

eighth_page = InlineKeyboardMarkup(row_width=5,
                                   inline_keyboard=[
                                       [
                                           InlineKeyboardButton(
                                               text='78. Әл-Мутәәли',
                                               callback_data=name_callback.new(greatest_name='78')
                                           )
                                       ],
                                       [
                                           InlineKeyboardButton(
                                               text='79. Әл-Барр',
                                               callback_data=name_callback.new(greatest_name='79')
                                           ),
                                           InlineKeyboardButton(
                                               text='80. Әт-Тәууәәб',
                                               callback_data=name_callback.new(greatest_name='80')
                                           ),
                                       ],
                                       [
                                           InlineKeyboardButton(
                                               text='81. Әл-Мунтәқим',
                                               callback_data=name_callback.new(greatest_name='81')
                                           ),
                                           InlineKeyboardButton(
                                               text='82. Әл-Афуу',
                                               callback_data=name_callback.new(greatest_name='82')
                                           ),
                                       ],
                                       [
                                           InlineKeyboardButton(
                                               text='83. Ар-Раууф',
                                               callback_data=name_callback.new(greatest_name='83')
                                           ),
                                           InlineKeyboardButton(
                                               text='84. Мәәликул-мулк',
                                               callback_data=name_callback.new(greatest_name='84')
                                           ),
                                       ],
                                       [
                                           InlineKeyboardButton(
                                               text='85. Зул-жәләли уал-икрам',
                                               callback_data=name_callback.new(greatest_name='85')
                                           ),
                                           InlineKeyboardButton(
                                               text='86. Әл-Муқсит',
                                               callback_data=name_callback.new(greatest_name='86')
                                           ),
                                       ],
                                       [
                                           InlineKeyboardButton(
                                               text='87. Әл-Жаамиғ',
                                               callback_data=name_callback.new(greatest_name='87')
                                           ),
                                           InlineKeyboardButton(
                                               text='88. Әл-Ғаний',
                                               callback_data=name_callback.new(greatest_name='88')
                                           )
                                       ],
                                       [
                                           InlineKeyboardButton(
                                               text='«1',
                                               callback_data=go_to.new(page='page_1')
                                           ),
                                           InlineKeyboardButton(
                                               text='‹ 6',
                                               callback_data=go_to.new(page='page_6')
                                           ),
                                           InlineKeyboardButton(
                                               text='7',
                                               callback_data=go_to.new(page='page_7')
                                           ),
                                           InlineKeyboardButton(
                                               text='•8•',
                                               callback_data=go_to.new(page='page_8')
                                           ),
                                           InlineKeyboardButton(
                                               text='9',
                                               callback_data=go_to.new(page='page_9')
                                           )
                                       ]
                                   ])

# ------------------------------InlineKeyboardMarkup Ninth Page ------------------------------------------

ninth_page = InlineKeyboardMarkup(row_width=5,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(
                                              text='89. Әл-Муғний',
                                              callback_data=name_callback.new(greatest_name='89')
                                          )
                                      ],
                                      [
                                          InlineKeyboardButton(
                                              text='90. Әл-Мааниғ',
                                              callback_data=name_callback.new(greatest_name='90')
                                          ),
                                          InlineKeyboardButton(
                                              text='91. Ад-Даарр',
                                              callback_data=name_callback.new(greatest_name='91')
                                          ),
                                      ],
                                      [
                                          InlineKeyboardButton(
                                              text='92. Ән-Наафиғ',
                                              callback_data=name_callback.new(greatest_name='92')
                                          ),
                                          InlineKeyboardButton(
                                              text='93. Ән-Нуур',
                                              callback_data=name_callback.new(greatest_name='93')
                                          ),
                                      ],
                                      [
                                          InlineKeyboardButton(
                                              text='94. Әл-Һәәди',
                                              callback_data=name_callback.new(greatest_name='94')
                                          ),
                                          InlineKeyboardButton(
                                              text='95. Әл-Бәдииғ',
                                              callback_data=name_callback.new(greatest_name='95')
                                          ),
                                      ],
                                      [
                                          InlineKeyboardButton(
                                              text='96. Әл-Баақи',
                                              callback_data=name_callback.new(greatest_name='96')
                                          ),
                                          InlineKeyboardButton(
                                              text='97. Әл-Уаарис',
                                              callback_data=name_callback.new(greatest_name='97')
                                          ),
                                      ],
                                      [
                                          InlineKeyboardButton(
                                              text='98. Ар-Рашиид',
                                              callback_data=name_callback.new(greatest_name='98')
                                          ),
                                          InlineKeyboardButton(
                                              text='99. Ас-Сабуур',
                                              callback_data=name_callback.new(greatest_name='99')
                                          )
                                      ],
                                      [
                                          InlineKeyboardButton(
                                              text='«1',
                                              callback_data=go_to.new(page='page_1')
                                          ),
                                          InlineKeyboardButton(
                                              text='‹ 6',
                                              callback_data=go_to.new(page='page_6')
                                          ),
                                          InlineKeyboardButton(
                                              text='7',
                                              callback_data=go_to.new(page='page_7')
                                          ),
                                          InlineKeyboardButton(
                                              text='8',
                                              callback_data=go_to.new(page='page_8')
                                          ),
                                          InlineKeyboardButton(
                                              text='•9•',
                                              callback_data=go_to.new(page='page_9')
                                          )
                                      ]
                                  ])
