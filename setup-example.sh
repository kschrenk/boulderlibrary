# ------------------------------------------- #
# Necessary env variables for local dev

export DATABASE_URL= 'postgresql://schrenkk@localhost:5432/boulderlibrary'
export SQLALCHEMY_TRACK_MODIFICATIONS=False

# ------------------------------------------- #
# Testing

export DATABASE_BASE_URL='postgresql://schrenkk@localhost:5432/'
export DATABASE_TEST_NAME='boulderlibrary_test'

# Tokens
export ADMIN_TOKEN='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1FWkROREJGUWtWR1JrWXlRelJHTURnNE1qZzBPVFEwUlRNMU1qRXdSVE0wUmpFNU56Y3pNZyJ9.eyJpc3MiOiJodHRwczovL2Rldi13ZDcxNGQ4aC5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVhNjgyZGFlN2I2YjkwYmY4MTg3MTdiIiwiYXVkIjoiYm91bGRlciIsImlhdCI6MTU5MDM4MDg5OSwiZXhwIjoxNTkwMzg4MDk5LCJhenAiOiJYZGx3NXRMRlJ0aGpoOW81N2UyNUhuRnlqSWttM0RkaCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiY3JlYXRlOmd5bXMiLCJkZWxldGU6Z3ltcyIsInVwZGF0ZTpneW1zIl19.Q3cegSv38aC98zunZBmbrzn26-Piknyb0TCMOEDLC0FvO5RvpU0IWEmZ-pxuRwa5UibCaSb20ysb4Rycv_HG3fEgJ61Ui2z4vqpcJX67BODumz7qJo_Dq4yT0djOf9Nvs9XTurm2iSL-qM6xv30LniA1-QO9-Qurx6ftvE2pj3cB4WWAnlY9XQ9fhLI0rxAIW1CDvgYEBboD80PcB69ahAWx0YSRMpIJKoyXFBTLU5e_q035VGPK2NGcOv4boPoIsFrCMYQufIyOp9S98Xr9YlvOB07CBGCp2yXrXFRZ57zodNSNpOQbzDHtOa5Eq5NFy9Ls6B5JRCD3DsTLI-XSvA'
export USER_TOKEN='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1FWkROREJGUWtWR1JrWXlRelJHTURnNE1qZzBPVFEwUlRNMU1qRXdSVE0wUmpFNU56Y3pNZyJ9.eyJpc3MiOiJodHRwczovL2Rldi13ZDcxNGQ4aC5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVjMzc4MDU0MDdmMjgwYmVkYjMwZTRjIiwiYXVkIjoiYm91bGRlciIsImlhdCI6MTU5MDM4MzczOCwiZXhwIjoxNTkwMzkwOTM4LCJhenAiOiJYZGx3NXRMRlJ0aGpoOW81N2UyNUhuRnlqSWttM0RkaCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZmF2b3I6Z3ltcyIsImdldDpmYXZvdXJpdGVfZ3ltcyIsInJlbW92ZTpmYXZvdXJpdGVfZ3ltcyJdfQ.pm2sWwPTCKmxDr5Q6u0CMUULqf4JVGKDwhZBSqt9u-3HRYD0O4XFZyCLp-BI7JhH6G_WxBbVrub2ru27Q7krOOG6fm3MYZfdy52I4XyDBtvQb4PVtjHkC0azo_IZQoRjHQFXCnocPuYhNHjfxuymVBktJmen6bP-iCtEh8ZKq3goGbQtlC6oh998CqUWsGK8nkqrc7I10gGpdMLE1Rnrq_YIszqTIs6c_Iyi8Ihqcly1BFtlQXKIx39E9sKVapG2LgvFGSRYLcQ0PXpoULBDfJvMzcf3Dky3b7YZSUCA5Fy15Tj8oVN8zRBJ3gypr2fYadaImyq0ti-XTNs7KBzhdQ'

# ------------------------------------------- #
# Flask (optional)

# Run flask in development mode
export FLASK_APP=app.py
export FLASK_DEBUG=True
export FLASK_ENV=development

