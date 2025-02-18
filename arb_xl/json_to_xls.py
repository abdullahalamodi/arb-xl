from pathlib import Path
import pandas as pd
import json
from arb_xl.logger import logger

def json_to_xls(json_files, output_xls):
    try:
        logger.info(f"Starting JSON/ARB to XLS conversion: {json_files} -> {output_xls}")

        data = {}

        for json_file in json_files:
            with open(json_file, "r", encoding="utf-8") as f:
                content = json.load(f)

            # Determine language code: use _locale if .arb, otherwise use filename
            language = content.get("_locale", json_file.stem)
            logger.info(f"Processing {json_file} as {language}")

            # Store translations, ignoring metadata keys (starting with '@')
            for key, value in content.items():
                if not key.startswith("@"):  # Ignore .arb metadata
                    if key not in data:
                        data[key] = {}
                    data[key][language] = value

        # Convert to DataFrame
        df = pd.DataFrame.from_dict(data, orient="index").reset_index()
        df.columns = ["Key"] + list(df.columns[1:])  # Ensure "Key" is the first column

        # Save to Excel
        df.to_excel(output_xls, index=False)
        logger.info(f"Successfully saved XLS file: {output_xls}")

    except Exception as e:
        logger.error(f"Error converting JSON/ARB to XLS: {e}", exc_info=True)
