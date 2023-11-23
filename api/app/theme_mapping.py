THEME_TO_GROUP: dict[str, str] = {
    'Отлов безнадзорных собак и кошек': 'Безопасность',
    'Безопасность общественных пространств': 'Безопасность',
    'Беженцы': 'Безопасность',
    'Предложение по благоустройству': 'Благоустройство',
    'Неисправные фонари освещения': 'Благоустройство',
    'Ненадлежащее состояние фасадов нежилых зданий, объектов и ограждений': 'Благоустройство',
    'Нарушение правил уборки внутридворового проезда, пешеходной дорожки': 'Благоустройство',
    'Уборка территорий': 'Благоустройство',
    'Нарушение правил уборки от снега и наледи территории парка и сквера': 'Благоустройство',
    'Нарушение правил проведения земляных работ': 'Благоустройство',
    'Обустройство асфальтового покрытия парковки, внутридворового проезда, тротуара, пешеходной дорожки, въезда во двор': 'Благоустройство',
    'Благоустройство придомовых территорий': 'Благоустройство',
    'Ненадлежащее содержание зеленых насаждений (газонов)/деревьев и кустарников': 'Благоустройство',
    'Ямы во дворах': 'Благоустройство',
    'Подтопление территории': 'Благоустройство',
    'Благоустройство общественного пространства (парк, сквер, пешеходная зона, бульвар, набережная, центральная улица или площадь)': 'Благоустройство',
    'Ненадлежащее состояние игровых элементов на детской или спортивной площадке': 'Благоустройство',
    'Парки и зоны отдыха': 'Благоустройство',
    'Борщевик Сосновского': 'Благоустройство',
    'Нарушение правил уборки от снега и наледи детской игровой и спортивной площадки': 'Благоустройство',
    'Нарушение правил уборки и вывоза загрязненного снега и наледи на газоне': 'Благоустройство',
    'Нарушение правил уборки от снега и наледи внутридворового проезда, тротуара, площади': 'Благоустройство',
    'Самовольная установка ограждений на территории общего пользования': 'Благоустройство',
    'Вырубка деревьев, кустарников': 'Благоустройство',
    'Открытые канализационные люки': 'Благоустройство',
    'Отсутствие фонарей освещения': 'Благоустройство',
    'Парковка на газонах': 'Благоустройство',
    'Отсутствие урн, лавочек в общественных местах и дворовой территории': 'Благоустройство',
    'Отсутствие общественных туалетов': 'Благоустройство',
    'Установка ограждений, препятствующих въезду на тротуар, газон на дворовой территории МКД': 'Благоустройство',
    'Разрушение тротуаров и пешеходных дорожек': 'Благоустройство',
    'Отсутствие детских площадок': 'Благоустройство',
    'Нарушение правил уборки и вывоза порубочных остатков': 'Благоустройство',
    'Запрос на газификацию и её условия': 'Газ и топливо',
    'Стоимость, оплата и возврат средств на газификацию': 'Газ и топливо',
    'Восстановление газоснабжения': 'Газ и топливо',
    'Сроки газификации': 'Газ и топливо',
    'Региональное имущество': 'Государственная собственность',
    'Несоблюдение правил уборки проезжей части': 'Дороги',
    'Нарушение правил очистки дорог от снега и наледи/Обращения о необходимости очистить тротуар от снега и наледи': 'Дороги',
    'Некачественно нанесенная разметка на проезжей части': 'Дороги',
    'Предложить установку нового лежачего полицейского (ИДН)': 'Дороги',
    'Несанкционированное ограничение движения, помехи движению, захват земли в полосе отвода автодорог': 'Дороги',
    'Ямы и выбоины на дороге': 'Дороги',
    'Нарушение технологии и (или) сроков производства работ': 'Дороги',
    'Предложение дороги в план ремонта': 'Дороги',
    'Подтопление автомобильных дорог': 'Дороги',
    'Ремонт/строительство мостов': 'Дороги',
    'Ливневые канализации (строительство и реконструкция)': 'Дороги',
    'Организация парковок': 'Дороги',
    'Содержание, ремонт и обустройство тротуаров': 'Дороги',
    'Некачественно выполненный ремонт дорог': 'Дороги',
    'Строительство или реконструкция дорог': 'Дороги',
    'Содержание дорожных знаков/Установка новых дорожных знаков, с внесением в схему дислокации, замена старых знаков на новые': 'Дороги',
    'Освещение неисправно или отсутствует': 'Дороги',
    'Организация переходов, светофоров/Изменить организацию движения': 'Дороги',
    'Ремонт дороги': 'Дороги',
    'Необходима установка и замена дорожных ограждений': 'Дороги',
    'Работа светофора (установка, изменение режима работы, оборудование кнопкой вызова)': 'Дороги',
    'Пробки': 'Дороги',
    'Наледь и сосульки на кровле': 'ЖКХ',
    'Сборы за капитальный ремонт': 'ЖКХ',
    'Плохое качество воды': 'ЖКХ',
    'Отсутствие горячей воды': 'ЖКХ',
    'Ремонт подъездов': 'ЖКХ',
    'Ненадлежащее содержание и эксплуатация МКД': 'ЖКХ',
    'Отсутствие электричества': 'ЖКХ',
    'Затопление подъездов, подвальных помещений': 'ЖКХ',
    'Подключение к водоснабжению': 'ЖКХ',
    'Перепланировка и реконструкция помещений': 'ЖКХ',
    'Залитие квартиры': 'ЖКХ',
    'Неисправность выступающих конструкций: балконов, козырьков, эркеров, карнизов входных крылец и т. п.': 'ЖКХ',
    'Ненадлежащее качество или отсутствие отопления': 'ЖКХ',
    'Другие проблемы с общедомовой системой водоотведения (канализации)': 'ЖКХ',
    'Лифт неисправен или отключен': 'ЖКХ',
    'Протечки с кровли (системы водостока)': 'ЖКХ',
    'Отсутствие холодной воды': 'ЖКХ',
    'Завышение платы за коммунальные услуги': 'ЖКХ',
    'Прорыв трубы/трубопровода': 'ЖКХ',
    'Засор в общедомовой системе водоотведения (канализации)': 'ЖКХ',
    'Жалобы на управляющие компании': 'ЖКХ',
    'Дезинфекция МКД': 'ЖКХ',
    'Некачественный капитальный ремонт': 'ЖКХ',
    'Несанкционированные надписи, рисунки, реклама на фасаде МКД': 'ЖКХ',
    'Плата за ЖКУ и работа ЕИРЦ': 'ЖКХ',
    'Ненадлежащая уборка подъездов и лифтов': 'ЖКХ',
    'Низкая температура воды/слабое давление': 'ЖКХ',
    'Непригодные для проживания жилые помещения': 'ЖКХ',
    'Нехватка материально-технического обеспечения': 'Здравоохранение/Медицина',
    'Отсутствие аптек': 'Здравоохранение/Медицина',
    'Отсутствие лекарств в аптеках': 'Здравоохранение/Медицина',
    'Социальная поддержка медперсонала': 'Здравоохранение/Медицина',
    'Очередь': 'Здравоохранение/Медицина',
    'Нехватка или сокращение врачей и медицинских учреждений': 'Здравоохранение/Медицина',
    'Диспансеризация': 'Здравоохранение/Медицина',
    'Льготные лекарства': 'Здравоохранение/Медицина',
    'Хамство медицинских работников': 'Здравоохранение/Медицина',
    'Отсутствие лекарств в стационарах': 'Здравоохранение/Медицина',
    'Просьбы о лечении': 'Здравоохранение/Медицина',
    'Скорая помощь': 'Здравоохранение/Медицина',
    'Предложения по созданию лечебных центров': 'Здравоохранение/Медицина',
    'Технические проблемы с записью на прием к врачу': 'Здравоохранение/Медицина',
    'Здравоохранение прочее': 'Здравоохранение/Медицина',
    'Оказание медицинской помощи не в полном объеме/отказ в оказании медицинской помощи': 'Здравоохранение/Медицина',
    'Питание в медицинских учреждениях': 'Здравоохранение/Медицина',
    'Вакцинация': 'Здравоохранение/Медицина',
    'Содержание больниц': 'Здравоохранение/Медицина',
    'Ошибки врачей, халатность': 'Здравоохранение/Медицина',
    'Низкая заработная плата врачей': 'Здравоохранение/Медицина',
    'Профильный осмотр': 'Здравоохранение/Медицина',
    'Тесты на коронавирус': 'Коронавирус',
    'Доступность вакцин': 'Коронавирус',
    'Сертификаты и QR-коды': 'Коронавирус',
    'Порядок и пункты вакцинации': 'Коронавирус',
    'Самоизоляция и карантин': 'Коронавирус',
    'Жалобы на врачей': 'Коронавирус',
    'Коронавирусные ограничения': 'Коронавирус',
    'Коронавирус': 'Коронавирус',
    'Проблемы в работе горячих линий': 'Коронавирус',
    'Учреждения культуры': 'Культура',
    'Культурно-досуговые мероприятия': 'Культура',
    'Государственные услуги': 'МФЦ "Мои документы"',
    'МФЦ "Мои документы"': 'МФЦ "Мои документы"',
    'Поддержка семей мобилизованных': 'Мобилизация',
    'Зарплата, компенсации, поощрения, выплаты': 'Мобилизация',
    'Плата за вывоз ТКО': 'Мусор/Свалки/ТКО',
    'Проблемы с контейнерами': 'Мусор/Свалки/ТКО',
    'Выброс мусора нарушителем': 'Мусор/Свалки/ТКО',
    'Стихийные свалки в городе/в парках/в лесу': 'Мусор/Свалки/ТКО',
    'Раздельная сортировка отходов': 'Мусор/Свалки/ТКО',
    'Строительство объектов по обращению с отходами': 'Мусор/Свалки/ТКО',
    'Уборка/Вывоз мусора': 'Мусор/Свалки/ТКО',
    'Отсутствие контейнерной площадки/Проезд к контейнерной площадке': 'Мусор/Свалки/ТКО',
    'Выплаты стипендий': 'Образование',
    'Строительство школ, детских садов': 'Образование',
    'Дистанционное образование': 'Образование',
    'Зарплата учителей': 'Образование',
    'ВУЗы и ССУЗы': 'Образование',
    'Социальная поддержка учителей': 'Образование',
    'Кадровые перестановки': 'Образование',
    'Безопасность образовательного процесса': 'Образование',
    'Содержание гос. образовательных организаций': 'Образование',
    'Устройство в ДОУ': 'Образование',
    'Образовательный процесс': 'Образование',
    'Проблемы с отоплением детских садов и школ': 'Образование',
    'Детские оздоровительные лагеря': 'Образование',
    'Питание': 'Образование',
    'ЕГЭ, ОГЭ': 'Образование',
    'Общее впечатление': 'Образование',
    'Дополнительное образование': 'Образование',
    'Нехватка мест в школах': 'Образование',
    'Неудовлетворительные условия проезда в транспорте на действующем маршруте': 'Общественный транспорт',
    'Содержание остановок': 'Общественный транспорт',
    'Изменить или отменить маршрут': 'Общественный транспорт',
    'График движения общественного транспорта': 'Общественный транспорт',
    'Некорректное поведение водительского состава': 'Общественный транспорт',
    'Отсутствие остановочных пунктов': 'Общественный транспорт',
    'Добавить новый маршрут': 'Общественный транспорт',
    'Проблемы с социальными картами или проездными документами': 'Общественный транспорт',
    'Пешеходные переходы и жд переезды': 'Общественный транспорт',
    'Изменение класса и количества автобусов': 'Общественный транспорт',
    'Льготы на проезд и тарифы': 'Общественный транспорт',
    'Памятники и объекты культурного наследия': 'Памятники и объекты культурного наследия',
    'Погребение и похоронное дело': 'Погребение и похоронное дело',
    'Санитарно-эпидемиологическое благополучие': 'Роспотребнадзор',
    'Обработка и уничтожение грызунов (дератизация)': 'Роспотребнадзор',
    'Информационно-техническая поддержка': 'Связь и телевидение',
    'Занятость и трудоустройство': 'Социальное обслуживание и защита',
    'Улучшение жилищных условий': 'Социальное обслуживание и защита',
    'Матери-одиночки, подростки': 'Социальное обслуживание и защита',
    'Инвалиды': 'Социальное обслуживание и защита',
    'Аварийное жилье/переселение': 'Социальное обслуживание и защита',
    'Дети и многодетные семьи': 'Социальное обслуживание и защита',
    'Соц.обслуживание прочее': 'Социальное обслуживание и защита',
    'Волонтерство': 'Социальное обслуживание и защита',
    'Оказание гос. соц. помощи': 'Социальное обслуживание и защита',
    'Задержка выплат гражданам': 'Социальное обслуживание и защита',
    'Социальные учреждения': 'Социальное обслуживание и защита',
    'Создание доступной среды для инвалидов': 'Социальное обслуживание и защита',
    'Пенсионеры и ветераны': 'Социальное обслуживание и защита',
    'Спецпроекты': 'Спецпроекты',
    'Строительство зданий': 'Строительство и архитектура',
    'Строительство социальных объектов': 'Строительство и архитектура',
    'Состояние зданий учреждений и организаций': 'Строительство и архитектура',
    'Архитектура города': 'Строительство и архитектура',
    'Нестационарная торговля (киоски, павильоны, сезонная торговля)': 'Торговля',
    'Строительство спортивной инфраструктуры': 'Физическая культура и спорт',
    'Спортивные мероприятия': 'Физическая культура и спорт',
    'Ремонт спортивных учреждений': 'Физическая культура и спорт',
    'Выбросы вредных веществ в атмосферу/загрязнение воздуха': 'Экология',
    'Выбросы вредных веществ в водоёмы/загрязнение водоёмов': 'Экология',
    'Цены и ценообразование': 'Экономика и бизнес',
    'Трудоустройство': 'Экономика и бизнес',
    'Качество электроснабжения': 'Электроснабжение',
    'Повреждение опор ЛЭП': 'Электроснабжение',
}
