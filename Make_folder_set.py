
#### 폴더 구조 설명 ####
#(** F : Folder)
#1. Dataset(F)  
#    1. Common(F) : 데이터셋 생성 및 데이터 전처리  
#        - Creat_dataset.py  
#        - Data_prep.py  
#        - Common_playground.ipynb  
#        - common_dataset.csv
#    2. PSO,ARA...(F) : Solution에 필요한 추가 데이터셋들  
#        - Create_minmax_dataset.py   
#        - min_max.csv
#2. Scaler(F) : 모델별 Sacler.bin 저장  
#        - model_a_standard_scaler.bin  
#        - etc
#3. Model(F) : 1,2차 학습 모델.pkl, 평가결과.img, 모델정보.txt 저장    
#    1. First_time(F) : 1차는 라이트한 모델별 결과  
#        1. Select_model.py : 정해진 모델별 분류,회기만 선택하여 모델 결과를 분류,회기내 폴더별 생성
#        2. Classification(F)   
#            - XGBoost(F)  
#                - Model.py  
#                - XGBoost_1st.pkl  
#                - Result(F)  
#                    - Evaluation.PNG  
#                - Info(F)  
#                    - Model_info.txt  
#        3. Regression(F)  
#            - XGBoost(F)
#                - Model.py  
#                - XGBoost_1st.pkl  
#                - Result(F)  
#                    - Evaluation.PNG  
#                - Info(F)  
#                    - Model_info.txt        
#    2. Second_time(F) : 2차는 1차에서 선별된 모델을 대상으로 그리드 서치 결과  
#        1. Grid_Search.py : 모델 선택, 모델 파라미터는 Config폴더에서 가져오기, 예상 시간 노티 해줄 수 있는 방법 고민해보기  
#        2. Select_model_train.py : 정해진 모델별 분류,회기만 선택하여 모델 결과를 분류,회기내 폴더별 생성    
#        ==> 위 두개 부분 좀 더 고민 필요  
#        3. Classification(F)  
#            - XGBoost(F)        
#                - Model.py  
#                - XGBoost_2nd.pkl  
#                - Result(F)  
#                    - Evaluation.PNG  
#                - Info(F)  
#                    - Model_info.txt        
#        4. Regression(F)  
#            - XGBoost(F)        
#                - Model.py  
#                - XGBoost_2nd.pkl  
#                - Result(F)  
#                    - Evaluation.PNG  
#                - Info(F)  
#                    - Model_info.txt    
#4. Prediction(F)  
#    1. Select_model_pred.py : 정해진 모델별 분류,회기만 선택하여 모델 결과를 분류,회기내 폴더별 생성  
#    2. Classification(F)  
#        - Pred_result.csv  
#    3. Regression(F)  
#        - Pred_result.csv  
#5. Solution(F)  
#    1. PSO(F) : PSO 동작에 요구되는 알고리즘 포함  
#    2. ARA(F) : 연관성 탐색 및 추천 동작에 요구되는 알고리즘 포함  
#    3. Recommondation(F) : 추천서비스 동작에 요구되는 알고리즘 포함  
#    4. etc  
#6. Config(F) : 코드 입력에 변경 사항 총괄  
#    1. config.ini
#7. Query(F) : 쿼리 사용시 활용  
#    1. query.xml
#8. Log(F) : 코드 동작시 Log 저장  
#    1. project_a.log


import os

class FolderStructureCreator:
    
    def __init__(self, base_folder):
        self.base_folder = base_folder
        self.create_folder_structure()
        
    def create_folder_structure(self):
        # 1. Dataset(F)
        dataset_folder = os.path.join(self.base_folder, "Dataset")
        os.makedirs(dataset_folder, exist_ok=True)

        # 1-1. Common(F)
        common_folder = os.path.join(dataset_folder, "Common")
        os.makedirs(common_folder, exist_ok=True)

        # Files in 1-1. Common
        common_files = [
            "Create_dataset.py",
            "Data_prep.py",
            "Common_playground.ipynb"
        ]
        for file_name in common_files:
            with open(os.path.join(common_folder, file_name), 'w') as f:
                pass

        # 1-2. PSO,ARA...(F)
        pso_ara_folder = os.path.join(dataset_folder, "PSO")
        os.makedirs(pso_ara_folder, exist_ok=True)

        # Files in 1-2. PSO,ARA...
        pso_ara_files = [
            "Create_minmax_dataset.py"
        ]
        for file_name in pso_ara_files:
            with open(os.path.join(pso_ara_folder, file_name), 'w') as f:
                pass

        # 2. Scaler(F)
        scaler_folder = os.path.join(base_folder, "Scaler")
        os.makedirs(scaler_folder, exist_ok=True)

        # 3. Model(F)
        model_folder = os.path.join(base_folder, "Model")
        os.makedirs(model_folder, exist_ok=True)

        # 3-1. First_time(F)
        first_time_folder = os.path.join(model_folder, "First_time")
        os.makedirs(first_time_folder, exist_ok=True)

        # 3-1-1. Select_model.py
        with open(os.path.join(first_time_folder, "Select_model.py"), 'w') as f:
            pass

        # 3-1-2. Classification(F)
        classification_folder = os.path.join(first_time_folder, "Classification")
        os.makedirs(classification_folder, exist_ok=True)

        # 3-1-2-1. XGBoost(F)
        xgboost_folder = os.path.join(classification_folder, "XGBoost")
        os.makedirs(xgboost_folder, exist_ok=True)

        # Files in 3-1-2-1. XGBoost
        xgboost_files = [
            "Model.py"
        ]
        for file_name in xgboost_files:
            with open(os.path.join(xgboost_folder, file_name), 'w') as f:
                pass

        # 3-1-2-1-1. Result(F)
        result_folder = os.path.join(xgboost_folder, "Result")
        os.makedirs(result_folder, exist_ok=True)

        # 3-1-2-1-2. Info(F)
        info_folder = os.path.join(xgboost_folder, "Info")
        os.makedirs(info_folder, exist_ok=True)

        # 3-1-3. Regression(F)
        regression_folder = os.path.join(first_time_folder, "Regression")
        os.makedirs(regression_folder, exist_ok=True)

        # 3-1-3-1. XGBoost(F)
        xgboost_folder = os.path.join(regression_folder, "XGBoost")
        os.makedirs(xgboost_folder, exist_ok=True)

        # Files in 3-1-3-1. XGBoost
        xgboost_files = [
            "Model.py"
        ]
        for file_name in xgboost_files:
            with open(os.path.join(xgboost_folder, file_name), 'w') as f:
                pass

        # 3-1-3-1-1. Result(F)
        result_folder = os.path.join(xgboost_folder, "Result")
        os.makedirs(result_folder, exist_ok=True)

        # 3-1-3-1-2. Info(F)
        info_folder = os.path.join(xgboost_folder, "Info")
        os.makedirs(info_folder, exist_ok=True)

        # 3-2. Second_time(F)
        second_time_folder = os.path.join(model_folder, "Second_time")
        os.makedirs(second_time_folder, exist_ok=True)

        # 3-2-1. Grid_Search.py
        with open(os.path.join(second_time_folder, "Grid_Search.py"), 'w') as f:
            pass

        # 3-2-2. Select_model_train.py
        with open(os.path.join(second_time_folder, "Select_model_train.py"), 'w') as f:
            pass

        # 3-2-3. Classification(F)
        classification_folder = os.path.join(second_time_folder, "Classification")
        os.makedirs(classification_folder, exist_ok=True)

        # 3-2-3-1. XGBoost(F)
        xgboost_folder = os.path.join(classification_folder, "XGBoost")
        os.makedirs(xgboost_folder, exist_ok=True)

        # Files in 3-2-3-1. XGBoost
        xgboost_files = [
            "Model.py"
        ]
        for file_name in xgboost_files:
            with open(os.path.join(xgboost_folder, file_name), 'w') as f:
                pass

        # 3-2-3-1-1. Result(F)
        result_folder = os.path.join(xgboost_folder, "Result")
        os.makedirs(result_folder, exist_ok=True)

        # 3-2-3-1-2. Info(F)
        info_folder = os.path.join(xgboost_folder, "Info")
        os.makedirs(info_folder, exist_ok=True)

        # 3-2-4. Regression(F)
        regression_folder = os.path.join(second_time_folder, "Regression")
        os.makedirs(regression_folder, exist_ok=True)

        # 3-2-4-1. XGBoost(F)
        xgboost_folder = os.path.join(regression_folder, "XGBoost")
        os.makedirs(xgboost_folder, exist_ok=True)

        # Files in 3-2-4-1. XGBoost
        xgboost_files = [
            "Model.py"
        ]
        for file_name in xgboost_files:
            with open(os.path.join(xgboost_folder, file_name), 'w') as f:
                pass

        # 3-2-4-1-1. Result(F)
        result_folder = os.path.join(xgboost_folder, "Result")
        os.makedirs(result_folder, exist_ok=True)

        # 3-2-4-1-2. Info(F)
        info_folder = os.path.join(xgboost_folder, "Info")
        os.makedirs(info_folder, exist_ok=True)

        # 4. Prediction(F)
        prediction_folder = os.path.join(base_folder, "Prediction")
        os.makedirs(prediction_folder, exist_ok=True)

        # 4-1. Select_model_pred_test.py
        with open(os.path.join(prediction_folder, "Select_model_pred_test.py"), 'w') as f:
            pass
        # 4-2. Select_model_pred_unseen.py
        with open(os.path.join(prediction_folder, "Select_model_pred_unseen.py"), 'w') as f:
            pass

        # 4-3. Classification_test(F)
        classification_folder = os.path.join(prediction_folder, "Classification_test")
        os.makedirs(classification_folder, exist_ok=True)

        # 4-4. Regression_test(F)
        regression_folder = os.path.join(prediction_folder, "Regression_test")
        os.makedirs(regression_folder, exist_ok=True)
        
        # 4-3. Classification_unseen(F)
        classification_folder = os.path.join(prediction_folder, "Classification_unseen")
        os.makedirs(classification_folder, exist_ok=True)

        # 4-4. Regression_unseen(F)
        regression_folder = os.path.join(prediction_folder, "Regression_unseen")
        os.makedirs(regression_folder, exist_ok=True)

        # 5. Solution(F)
        solution_folder = os.path.join(base_folder, "Solution")
        os.makedirs(solution_folder, exist_ok=True)

        # 5-1. PSO(F), 5-2. ARA(F), 5-3. Recommondation(F), 5-4. etc
        solution_subfolders = ["PSO"]
        for subfolder_name in solution_subfolders:
            subfolder_path = os.path.join(solution_folder, subfolder_name)
            os.makedirs(subfolder_path, exist_ok=True)

        # 6. Config(F)
        config_folder = os.path.join(base_folder, "Config")
        os.makedirs(config_folder, exist_ok=True)

        # 6-1. config.ini
        with open(os.path.join(config_folder, "config.ini"), 'w') as f:
            pass

        # 7. Query(F)
        query_folder = os.path.join(base_folder, "Query")
        os.makedirs(query_folder, exist_ok=True)

        # 7-1. query.xml
        with open(os.path.join(query_folder, "query.xml"), 'w') as f:
            pass

        # 8. Log(F)
        log_folder = os.path.join(base_folder, "Log")
        os.makedirs(log_folder, exist_ok=True)

        # 8-1. project_a.log
        with open(os.path.join(log_folder, "project_a.log"), 'w') as f:
            pass
    
current_directory = os.getcwd()
print("현재 경로:", current_directory)
    
#base_folder = 'C:/Workspace/HANSBAR/' 
base_folder = current_directory
folder_creator = FolderStructureCreator(base_folder)