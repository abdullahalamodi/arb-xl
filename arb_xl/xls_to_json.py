from pathlib import Path
import pandas as pd
import json
from arb_xl.logger import logger

def xls_to_json(xls_file, output_dir, use_arb=False):
    try:
        logger.info(f"Starting XLS to {'ARB' if use_arb else 'JSON'} conversion: {xls_file} -> {output_dir}")

        df = pd.read_excel(xls_file)
        keys = df["Key"].tolist()
        languages = df.columns[1:]  # Exclude "Key"

        for lang in languages:
            output_path = Path(output_dir) / f"{lang}.{'arb' if use_arb else 'json'}"
            translations = {keys[i]: df[lang][i] for i in range(len(keys)) if pd.notna(df[lang][i])}

            # If saving as .arb, add _locale and metadata placeholder
            if use_arb:
                translations["_locale"] = lang
                new_entries = {}
                for key in translations.keys():
                    new_entries[f"@{key}"] = {"description": "", "type": "text"} 
                translations.update(new_entries)

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(translations, f, indent=2, ensure_ascii=False)

            logger.info(f"Saved {'ARB' if use_arb else 'JSON'} file: {output_path}")

    except Exception as e:
        logger.error(f"Error converting XLS to {'ARB' if use_arb else 'JSON'}: {e}", exc_info=True)
